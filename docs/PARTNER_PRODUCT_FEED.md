# FRONTERA partner product feed guide

This document defines the product data format used by the FRONTERA product finder and expedition inventory matcher.

## Important publishing rule

Only publish products when FRONTERA has permission to use the product information and image, a current product destination URL, and an approved affiliate or other clearly disclosed commercial relationship where applicable. Never invent a product, price, stock status, rating, test result, or endorsement. The public catalog currently remains intentionally empty until approved listings are ready.

## File location

The public catalog is `data/products.json`. It must remain valid JSON and use this top-level structure:

```json
{
  "updated_at": "2026-11-25",
  "products": []
}
```

## Product fields

| Field | Required? | Format / guidance |
| --- | --- | --- |
| `name` | Yes | Exact product name supplied by the brand or retailer. |
| `brand` | Yes | Brand or authorized retailer name. |
| `description` | Yes | Accurate, concise product description based on approved source material. |
| `category` | Yes | One of the category values below. |
| `url` | Yes | Full HTTPS product URL. Use the approved affiliate tracking URL only after the program authorizes it. |
| `price` | No | Numeric USD price only when supplied and recently verified. Leave null when unavailable. |
| `image` | No | Full HTTPS image URL that FRONTERA is permitted to display. Leave blank or null if unavailable. |
| `availability` | No | Seller-supplied availability wording, or “Check seller for availability.” |
| `updated_at` | Recommended | ISO date, YYYY-MM-DD, for the latest verification of price and listing details. |
| `features` | No | Array of accurate product features useful for search. |
| `tags` | No | Array of relevant search terms. |
| `activities` | No | Activities this product genuinely supports. |
| `terrain` | No | Terrain or environments for which the product is suitable, based on seller specifications. |
| `climate` | No | Climate tags supported by product specifications. |
| `featured` | No | Boolean editorial flag; never use this to imply paid placement is an independent recommendation. |

## Allowed category values

- `shelter` — tents, tarps, shelters
- `sleep` — sleeping bags, pads, sleep systems
- `cook` — camp stoves, cookware, grills, utensils
- `trail` — packs, hiking and trail equipment
- `light` — lanterns, headlamps, portable power
- `water` — water storage, filtration, hydration
- `food` — trail food, ingredients, seasonings
- `offroad` — overlanding and off-road equipment
- `marine` — watercraft and marine equipment
- `vehicles` — adventure vehicles and vehicle accessories
- `apparel` — clothing, footwear, protective layers
- `other` — relevant outdoor equipment not covered above

## Example record (illustrative only — do not publish as a real listing)

```json
{
  "name": "Example Camp Cook Set",
  "brand": "Example Outdoor Brand",
  "description": "Illustrative product description for a compact outdoor cook set.",
  "category": "cook",
  "url": "https://example.com/products/example-cook-set",
  "price": null,
  "image": null,
  "availability": "Check seller for availability",
  "updated_at": "2026-11-25",
  "features": ["nesting cookware", "camp cooking"],
  "tags": ["cook set", "camp kitchen"],
  "activities": ["Camping"],
  "terrain": ["campground", "backcountry"],
  "climate": [],
  "featured": false
}
```

The example uses a reserved example.com address and is not a real product. Do not copy it into the public catalog.

## Quality checks before publishing

1. Confirm the brand or retailer has approved the listing and image use.
2. Open every destination URL and verify it resolves to the exact product.
3. Confirm any affiliate URL is issued by the approved program and includes the required tracking.
4. Verify price, currency, availability wording, and update date; otherwise omit the price.
5. Confirm the category is one of the allowed values.
6. Check spelling, accessibility of the image, and that the description does not make unsupported performance or safety claims.
7. Validate the JSON before committing.
8. Recheck the listing periodically and remove or correct discontinued, redirected, or inaccurate products.

## FRONTERA editorial and disclosure standard

Listings should be relevant to outdoor use and presented with accurate source information. Paid placements must be clearly labeled as sponsored. Affiliate commissions must not be presented as evidence that a product is independently tested or endorsed. The retailer remains responsible for checkout, fulfillment, returns, warranties, and final product terms.
