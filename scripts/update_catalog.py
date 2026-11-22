#!/usr/bin/env python3
"""Refresh FRONTERA product data from approved JSON or CSV partner feeds."""
import csv, io, json, os, re, sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "data", "feeds.json")
OUTPUT = os.path.join(ROOT, "data", "products.json")
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

ALIASES = {
 "name": ["name", "title", "product_name", "product"],
 "brand": ["brand", "manufacturer", "vendor"],
 "price": ["price", "sale_price", "current_price", "amount"],
 "currency": ["currency", "price_currency"],
 "url": ["url", "link", "product_url", "affiliate_url", "tracking_url"],
 "image": ["image", "image_url", "image_link", "main_image"],
 "description": ["description", "short_description", "summary"],
 "category": ["category", "product_type", "frontera_category"],
 "availability": ["availability", "stock", "stock_status"],
 "sku": ["sku", "id", "product_id", "item_id"],
}

def normalize_category(value):
    value = str(value or "").lower()
    mapping = {
      "shelter": ("tent", "shelter", "canopy", "tarp"),
      "sleep": ("sleep", "sleeping bag", "pad", "mattress"),
      "cook": ("cook", "stove", "kitchen", "cookware", "grill"),
      "trail": ("backpack", "pack", "hiking", "trekking"),
      "light": ("light", "lantern", "headlamp", "power", "battery"),
      "water": ("water", "filter", "hydration", "purifier"),
      "food": ("food", "spice", "coffee", "seasoning", "snack"),
    }
    for category, words in mapping.items():
        if any(word in value for word in words):
            return category
    return "other"

def first(record, keys):
    for key in keys:
        if record.get(key) not in (None, ""):
            return record[key]
    return None

def map_record(record, field_map):
    lowered = {str(k).lower(): v for k, v in record.items()}
    result = {}
    for field, aliases in ALIASES.items():
        source = field_map.get(field)
        value = lowered.get(str(source).lower()) if source else first(lowered, aliases)
        if value is not None:
            result[field] = str(value).strip() if field != "price" else value
    if not result.get("name") or not result.get("url"):
        return None
    if not re.match(r"^https://", result["url"], re.I):
        return None
    try:
        result["price"] = float(re.sub(r"[^0-9.]", "", str(result["price"]))) if result.get("price") else None
    except ValueError:
        result["price"] = None
    result["category"] = normalize_category(result.get("category") or result.get("name"))
    result["updated_at"] = NOW
    result["source"] = "approved_partner_feed"
    return result

def fetch_feed(feed):
    request = Request(feed["url"], headers={"User-Agent": "FRONTERA-ProductCatalog/1.0"})
    with urlopen(request, timeout=45) as response:
        raw = response.read().decode("utf-8-sig")
    if feed.get("format", "json").lower() == "csv":
        records = list(csv.DictReader(io.StringIO(raw)))
    else:
        data = json.loads(raw)
        key = feed.get("products_key", "products")
        records = data if isinstance(data, list) else data.get(key, [])
    if not isinstance(records, list):
        raise ValueError("Feed did not contain a product list")
    products = []
    for record in records:
        if isinstance(record, dict):
            item = map_record(record, feed.get("field_map", {}))
            if item:
                products.append(item)
    return products

def main():
    with open(CONFIG, encoding="utf-8") as f:
        config = json.load(f)
    products, errors = {}, []
    for feed in config.get("feeds", []):
        try:
            for item in fetch_feed(feed):
                key = (item.get("brand", "") + "|" + item.get("sku", item["name"])).lower()
                products[key] = item
            print("Updated feed:", feed.get("name", "unnamed"))
        except Exception as exc:
            errors.append(f'{feed.get("name", "unnamed")}: {exc}')
            print("Feed error:", errors[-1], file=sys.stderr)
    output = {"updated_at": NOW, "products": list(products.values()), "feed_errors": errors}
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Catalog contains {len(products)} products.")
    # Do not silently replace a working catalog with an empty one when all feeds fail.
    if errors and not products and config.get("feeds"):
        raise SystemExit("All configured feeds failed; inspect logs before publishing.")

if __name__ == "__main__":
    main()
