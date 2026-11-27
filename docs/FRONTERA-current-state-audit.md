# FRONTERA — Current-State Audit

_Audit date: 27 November 2026_

This is a repository-level audit, not a successful end-to-end browser or production smoke test.

## Release/version status

- Repository: `freemoneyapex-Frontera1/Frontera-`
- Development branch: `shopping-experience-v1`
- Default-branch `index.html` blob SHA: `f43b4e451471bb3e24b2987e3269ce7db6ddb4c5`
- Development-branch `index.html` blob SHA: `5b17ea9985ed8c1672ef1ab3b7bfb1914425174a`
- The default-branch index is an older version: it does not contain the current “FRONTERA buying verdict” comparison implementation or the TopOak feed loader.
- The development branch contains the newer expedition planner, TopOak feed loader, verified-fit filtering and comparison verdict interface.
- The development branch has not been confirmed merged into the default branch.
- A live browser verification could not be completed during this audit. Therefore public-site reachability, exact deployed version, and live behavior remain unverified.

## Catalog and recommendation data

- Development branch contains a base `data/products.json` catalog with 26 products, updated 26 November 2026.
- The 26-product base file now has 7 verified rooftop-tent variants and 19 products still awaiting review.
- The first verified batch covers Vision (63/75 in), Stellar, Galaxy Pro, Nebula and Galaxy Light (51/56 in). Manufacturer-published dimensions, weights, occupancy, fabric/waterproof ratings and crossbar requirements were recorded where available.
- The 7 tent records are marked for vehicle-supported camping/overlanding and manufacturer-stated 4-season use. FRONTERA notes explicitly state that the season rating is manufacturer-provided, not an independent field test, and that vehicle/rack compatibility must be checked. No unsupported wind-speed or storm-safety claims were added.
- Development branch also contains `data/topoak-products.b64`, a compressed feed-derived product dataset. Earlier import processing reported 128 in-stock TopOak products; the site loader merges this feed with the 26-product base catalog and keeps base records first when product names match. The compressed payload was not independently recounted during this update.
- Product schema supports manufacturer specifications, fit-review status/source/date, environment/activity/condition fit, and comparison assessments.
- Taxonomy defines 8 environments, 18 activities and 18 categories.
- The recommendation filter is designed to exclude unverified products from expedition-specific matches. The catalog can be broad while the recommendation set remains narrow and evidence-based.
- Current comparison verdict is rules-based. It is not a live AI service. Product quality/value conclusions require populated, source-backed comparison assessments.

## Supplier pipeline

Five supplier records are currently in `data/supplier-pipeline.json` on the development branch:
- Sea to Summit — research lead; AvantLink; feed not confirmed.
- UCO Gear — research lead; AvantLink; feed not confirmed.
- Naturehike — research lead; Impact; feed not confirmed.
- Timber Ridge — research lead; Awin; feed not confirmed.
- OUTFITR (US) — research lead; Awin; feed not confirmed; keep on due-diligence hold until commission terms are reconciled.

These records are research leads, not confirmed approvals. TopOak is a separate Awin partner and its feed was imported on the development branch. AvantLink publisher ownership verification was still pending in the latest recorded status.

## Immediate release blockers / work items

1. Confirm GitHub Pages deployment source and verify which branch/version is actually served at the public URL.
2. Run a fresh mobile and desktop browser smoke test against the production URL and the development preview.
3. Reconcile base products and compressed TopOak feed: count, duplicates, stock, prices, image coverage, retailer URLs and affiliate tracking.
4. Continue product-fit review in category batches: awnings/shelters next, then vehicle accessories, water storage, sleep accessories and camp furniture. Use manufacturer or authoritative specifications.
5. Keep unverified products out of expedition-specific recommendations; explain empty results clearly.
6. Complete AvantLink website ownership verification and inspect merchant terms before applying.
7. Confirm supplier approval, feed permission and tracking separately before any additional import.
8. Check the public site's affiliate disclosure, privacy/terms/contact information and brand-clearance status before broader promotion.

## Audit limitations

- The browser automation run did not start because the connected browser-service wallet was out of funds; no browser test result is claimed.
- The web page open check did not return page content.
- This audit does not establish that the GitHub Pages site is currently reachable or identify the exact deployed build.
- Product prices and availability are time-sensitive and must be checked at the retailer before relying on them.
