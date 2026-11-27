# FRONTERA — Business & Development Roadmap

_Last updated: 27 November 2026_

## Vision

FRONTERA is an outdoor discovery and expedition-planning marketplace. It helps people find relevant gear, compare options, and prepare for adventures across different environments and activities. It is not a desert-only shop or a single-retailer storefront.

## Operating principles

1. **Relevance before volume:** A large catalog is useful only when products can be accurately discovered and filtered.
2. **Evidence before recommendations:** Do not claim a product is suitable for an environment or condition based only on its title, category, or affiliate status.
3. **Transparency:** Distinguish retailer-supplied facts, manufacturer specifications, FRONTERA assessments, and unknown information.
4. **No invented winners:** Best-value, premium, and quality verdicts require comparable, source-backed evidence.
5. **Retailer checkout:** Affiliate retailers handle checkout, shipping, returns, and customer service unless the business model deliberately changes.
6. **Launch safely:** Keep development separate from production until release checks pass.

## Roadmap at a glance

| Phase | Focus | Priority | Exit criteria |
|---|---|---:|---|
| 1 | Supplier network and catalog depth | Immediate | Multiple relevant suppliers researched; approvals and feed permissions tracked; products imported with provenance |
| 2 | Product verification and recommendation trust | Immediate | Verified fit records backed by HTTPS sources; unsupported products excluded from trip-specific recommendations |
| 3 | Expedition planner and comparison intelligence | High | Planner handles environments and conditions; comparison explains trade-offs without unsupported quality claims |
| 4 | Customer experience and trust | High | Mobile/desktop QA, clear affiliate disclosures, helpful destination and preparation content |
| 5 | Business operations and measurement | High | Analytics, affiliate tracking checks, supplier operations, support and privacy/legal basics |
| 6 | Audience growth and partnerships | Later | Repeat-visit content, creator/guide relationships, destination partnerships and measured acquisition |
| 7 | Experiences marketplace | Later | Validated partner supply for rentals, guided adventures, tours and other bookable experiences |

## Phase 1 — Supplier network and catalog depth

### Goals
- Expand beyond the current TopOak overlanding-heavy catalog.
- Build coverage across shelters, sleep systems, hiking/backpacking, camp kitchens, hydration/water treatment, navigation, lighting, weather protection, alpine/snow, fishing/paddling, vehicle recovery/storage/power, and other relevant categories.
- Preserve broad inventory while filtering recommendations to the actual trip.

### Supplier workflow
Track each supplier separately through these states:
1. Research lead
2. Application submitted
3. Approved by network/merchant
4. Product feed or permitted data source confirmed
5. Feed imported and normalized
6. Tracking/link validation passed
7. Active in catalog

Approval alone does not mean a feed is available or that products are verified for expedition use.

### Current known pipeline
- **TopOak Overland:** Awin advertiser approval was reported on 26 November 2026; feed imported with 128 in-stock records at that time. Recheck live price, stock, links and tracking periodically.
- **AvantLink:** Publisher application 1689141 was awaiting website ownership verification as of 27 November 2026. Do not treat the account as approved until confirmed.
- **Sea to Summit, UCO Gear, Naturehike, Timber Ridge:** Research leads only; application/approval/feed access must be confirmed before importing.
- **OUTFITR US:** Hold for commission/terms due diligence because available commission information was inconsistent.

### Phase 1 deliverables
- Supplier pipeline with owner, network, merchant ID, application status, approval date, feed status, commission, cookie/attribution terms, restrictions, last checked date and notes.
- Category coverage report showing strong, weak and missing inventory areas.
- Feed import checks for duplicates, out-of-stock items, missing images, invalid prices and broken affiliate links.
- Product provenance: supplier, source URL/feed, import date and last refresh date.

## Phase 2 — Product verification and recommendation trust

### Product evidence model
Keep these concepts separate:
- **Retail facts:** price, availability, images, retailer description and product URL.
- **Manufacturer specifications:** dimensions, weight, materials, temperature ratings, weather ratings, capacities, compatibility and care/installation requirements.
- **FRONTERA fit assessment:** environment, activity and conditions supported by evidence, with reviewer/date/source and limitations.
- **Comparison assessment:** quality/value conclusions with methodology, source evidence and review date.

### Recommendation guardrails
A product must not be recommended for a specific expedition unless its fit record is verified, current enough for the relevant claim, source-backed, and matches the selected environment, activity and conditions. If evidence is missing, show that no verified match is available rather than filling the space with weak matches.

### Initial verification order
1. Confirm product identity and exact model/variant.
2. Find manufacturer documentation or authoritative product specifications.
3. Record measurable specifications and compatibility constraints.
4. Assess environment/activity/condition fit only where evidence supports it.
5. Record source, reviewer and review date.
6. Recheck price/stock separately from fit verification.

## Phase 3 — Expedition planner and comparison intelligence

- Expand environment coverage: desert/arid, mountain/high country, alpine/snow, forest/woodland, coastal/beach, lakes/rivers and overlanding/off-road.
- Use trip conditions such as temperature, wind, precipitation and humidity; avoid stereotypes about a destination's climate.
- Improve packing lists and trip preparation guidance.
- Comparison should distinguish cheapest, best-supported value and premium options.
- Do not label a product “better quality” without a defensible, source-backed assessment.
- The current comparison verdict implementation is rules-based; a true AI layer is future work and must run securely server-side. Never expose API keys in browser code.

## Phase 4 — Customer experience and trust

- Test mobile and desktop layouts, search, filters, quick view, compare tray, comparison modal and planner.
- Confirm affiliate links open the correct retailer/product and preserve tracking.
- Show clear affiliate disclosures near relevant links.
- Explain why an item appears in a recommendation and disclose important limitations.
- Build useful destination guides, seasonal collections, checklists and outdoor cooking/camp-kitchen content.
- Keep checkout with the retailer and make that handoff clear.

## Phase 5 — Business operations and measurement

- Validate affiliate click attribution and conversion reporting where available.
- Track catalog freshness, broken links, out-of-stock rates, search terms, product clicks and planner completion.
- Establish supplier review cadence and a process for feed failures.
- Publish appropriate privacy, affiliate disclosure, terms and contact information.
- Complete brand/trademark clearance with qualified counsel before major public marketing or significant brand investment; this roadmap is not a legal clearance.

## Phase 6 — Audience growth and partnerships

- Publish practical expedition guides and destination-specific gear education.
- Build email/social content only when there is a clear value exchange and privacy-compliant consent.
- Develop relationships with outdoor creators, guides, campgrounds and destination operators.
- Measure which content and categories lead to useful product discovery, not just page views.

## Phase 7 — Experiences marketplace

Only after the gear discovery experience is reliable, explore:
- ATV and off-road rentals
- Guided hikes and outdoor adventures
- Paragliding and other activity providers
- Tours, cruises and destination experiences

Each experience category will need provider vetting, availability/booking integration, cancellation terms, safety information, insurance/liability review and clear responsibility boundaries.

## Immediate 30-day execution plan

### Week 1 — Establish the baseline
- Audit the current production site versus the development branch.
- Confirm the TopOak feed, prices, stock and affiliate links.
- Finish AvantLink ownership verification when the verification email is available.
- Review supplier pipeline status and prioritize category gaps.
- Produce a catalog coverage and data-quality report.

### Week 2 — Expand supplier coverage
- Complete due diligence on the highest-value supplier leads.
- Submit applications only when network verification and terms are understood.
- Confirm feed access and data-use permissions before importing.
- Normalize approved feeds and deduplicate products.

### Week 3 — Verify the highest-impact products
- Select a focused batch across major categories.
- Verify exact models and manufacturer specifications.
- Add evidence-backed fit assessments.
- Test that unverified products remain excluded from trip-specific recommendations.

### Week 4 — Customer-readiness review
- Run mobile/desktop and functional QA.
- Validate affiliate tracking and disclosures.
- Review comparison language and recommendation explanations.
- Resolve launch-blocking defects and prepare a controlled soft launch decision.

## Release gates

Do not merge the development branch into production or announce a full public launch until:
- The release candidate is tested on mobile and desktop.
- Core pages and catalog loading work reliably.
- Search, filters, Quick View, comparison and planner pass functional checks.
- Retailer links and affiliate disclosures are correct.
- No unsupported product-fit or quality claims are presented as verified.
- Known limitations and unavailable features are clearly communicated.
- Brand and legal risks have been reviewed to an appropriate level.

## Working status — 27 November 2026

- Development work is being maintained on `shopping-experience-v1`; do not assume it is the production version.
- The comparison verdict is currently rules-based, not a live AI service.
- TopOak feed data was imported; prices and availability require ongoing refresh.
- AvantLink ownership verification was pending.
- Supplier research leads are not the same as approved, feed-enabled partners.
- No production merge or public launch approval is implied by this roadmap.

## Next action

Create a current-state audit covering the production branch, development branch, catalog data quality, supplier pipeline, recommendation verification coverage and release blockers. Use that audit to set the exact Week 1 worklist.
