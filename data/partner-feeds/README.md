# FRONTERA partner product feeds

This folder contains normalized product feeds from approved merchant partners.

## Register a partner

1. Obtain permission and an approved affiliate tracking method from the merchant/network.
2. Create a JSON file named with a lowercase slug, for example `kemimoto.json`.
3. Use the normalized structure below.
4. Add an entry to `manifest.json` with the exact public brand name and the relative feed path.
5. Test the feed and product links before publishing.

```json
{
  "updated_at": "YYYY-MM-DD",
  "products": [
    {
      "name": "Product name",
      "brand": "Merchant brand",
      "description": "Accurate merchant-supplied product description",
      "category": "offroad",
      "subcategory": "ATV accessories",
      "url": "https://approved-affiliate-tracking-link",
      "price": 123.45,
      "image": "https://merchant-image-url",
      "availability": "In stock",
      "updated_at": "YYYY-MM-DD"
    }
  ]
}
```

Allowed categories: `shelter`, `sleep`, `apparel`, `footwear`, `cook`, `water`, `trail`, `light`, `power`, `navigation`, `safety`, `offroad`, `vehicles`, `storage`, `marine`, `fishing`, `food`, `other`.

The storefront requires a product name and an HTTPS purchase URL. Invalid records are skipped. A failed or unavailable partner feed is isolated: it must not prevent TopOak or other partner feeds from loading.

Do not add a merchant until its affiliate relationship and tracking links are approved. Do not invent prices, availability, product specifications, or images. Refresh prices and availability according to the merchant/network feed terms.
