# E-commerce: catalog → crawlable offers → feed consistency

## Input → output → validation

**Input:** catalog export (IDs, variants, price/currency, stock), URL/template map, feed/merchant diagnostics, markets/shipping/returns, inventory source of truth, permitted analytics and update cadence.
**Output:** [commerce-matrix.csv](../templates/commerce-matrix.csv), URL/indexability policy, discrepancy backlog, schema/feed DRAFT, pilot/read-back and business metrics.
**Validation:** chosen variant is purchasable exactly as advertised; page, markup, feed and checkout do not conflict; representative strata and edge states verified. No paid API or feed publish without approval.

## 1. Model and sample the catalog

Map category → subcategory → product family → variant SKU → offer/market. Separate informational comparison/affiliate page from seller checkout; merchant listing eligibility is not granted to any page containing Product markup.[17]
Choose a bounded sample covering major templates/categories, revenue/demand priorities, parameter variants, sale, out-of-stock, discontinued, multilingual/currency, mobile/JS and pagination. Record full universe counts and sampled count; do not call sample a full audit.
For each SKU preserve identifiers literally. Validate format first; never invent/repair GTIN/MPN to make validation pass. Attribute manufacturer vs merchant IDs correctly; reviews must be authentic and attributable.

## 2. URL and variant policy

Read actual selectors and direct deep links. Google can identify variants through separate URLs; fragment-only changes are not separate indexed pages.[9]
Distinguish two implementations before recommending canonicals:
- Single product page where query parameters preselect variants: define stable group/base canonical and ensure direct variant URL selects the correct purchasable offer.
- Separate meaningful variant pages: inspect the Google multi-page ProductGroup guidance and actual content/URLs; do not blindly canonicalize every page to a single group or force every parameter to self-canonical.[10]
Record intended canonical, actual canonical, internal links, sitemap URL, feed `link`/variant selection and any merchant canonical field separately. Conflicts need a documented policy, not search-and-replace.
For ProductGroup/hasVariant/variesBy/productGroupID use real data and current required properties. Group relationship markup does not fix nonfunctional selectors or invisible offers.[10]

## 3. Categories, facets and crawl control

1. Identify query parameters for filter/sort/tracking/session, pagination and invalid combinations; estimate URL explosion from real inventory, not guessed site size.
2. Decide which filtered pages deserve search landing pages: stable demand, sufficient inventory, useful distinct offer/context, maintainable URL. Everything else needs a reasoned crawl/index policy.
3. Read current faceted-navigation guidance. Canonical is not an efficient universal crawl-budget switch; robots blocks crawling, not guaranteed deindexing, and blocked pages cannot expose their noindex to that crawler.[22]
4. Separate deindexing plan from crawl suppression and from duplicate consolidation. No blanket robots/noindex before checking affected valuable URLs; approval and rollback required.
5. Keep allowed filters deterministic; test sort/filter order, empty/invalid combinations, infinite paths and pagination. Empty/nonexistent combinations need intentional behavior, not soft-404 infinite crawl.[22]
6. Product discovery must work through crawlable links/category pagination rather than search-form only or scroll-only UI. Route deeper decisions to `seo-site-architecture`/`technical-seo-audits`.

## 4. Product content and structured data

Verify title/variant/specs/dimensions, original useful description, compatible uses, safety warnings, shipping/returns and customer support. No fixed 200-word requirement, mandatory image count or title character count as a ranking rule.
Images: correct selected variant, accurate representation, rights, descriptive non-stuffed alt, responsive delivery and a usable primary image. Do not lazy-load the only above-fold product image by default without performance testing.
Validate JSON-LD syntax and Google's current merchant listing/product snippet requirements separately. Markup must match visible facts; unsupported type ≠ supported rich result. Never generate aggregateRating/review without genuine visible source. Rich Results Test PASS is eligibility feedback, not a promise of display.[17]

## 5. Stock and product lifecycle

| State | Proposed policy | Validation |
|---|---|---|
| Temporarily unavailable | Preserve useful page and honest availability; restock notice only if truthful | Page/schema/feed/checkout agree; no fake InStock |
| Backorder/preorder | Clear conditions and real expected date if known | Correct current feed enum, date and checkout terms |
| Permanently discontinued | Keep useful reference or route to a genuinely equivalent replacement; otherwise deliberate removal | No mass irrelevant redirects to homepage; internal links/feed/sitemap updated intentionally |
| Variant unavailable | Preserve other purchasable variants and selected state | Deep links do not silently sell a different SKU |
| Sale/price change | Single source of truth + sync schedule/latency owner | Currency, tax context, validity window and checkout price match |

These are decision patterns, not a universal instruction to 404 unavailable items. Batch changes require old/new URL policy and rollback.

## 6. Feed / Shopping reconciliation

Read-only Merchant Center export first: account/market, diagnostic codes, timestamp, affected IDs, ads vs free-listing destinations. A search snapshot does not prove Merchant eligibility; organic presence and paid/free Shopping are separate surfaces.
Join catalog, page, structured data, feed and selected-variant checkout by stable ID/market; compare exact price/currency/availability, landing URL, image, brand/identifiers, variant group, shipping and returns. Feed mismatches can prevent serving.[18]
Capture refresh schedule, last successful feed/import time, inventory lag and responsible system. Auto updates are not a substitute for truthful consistent source data.
Current product-data requirements vary by attribute/product/market; verify each required/conditional attribute in official docs, including AI-generated asset/text metadata when applicable. Do not reuse a stale schema checklist as feed specification.[18]
Recommendations to enable ads/bid/spend are out of audit scope; show budget and get explicit confirmation. APIs require current discovery; do not copy donor endpoint names or obsolete Shopping API integrations.

## 7. Pilot, verification and measurement

Preview exact affected IDs/fields/URLs and merchant destination, errors fixed, rollback, approval. Validate staging, then authorized pilot; read back the public page/rendered offer and exact feed/merchant record. Import accepted ≠ item approved ≠ impression observed; document pending states.
Metrics: eligible item counts/errors, indexable product/category cohorts, query/country performance, product clicks, add-to-cart/purchases/margin where authorized. Track stock/price/campaign seasonality as confounders. Failed checkout/no stock can invalidate traffic growth as success.

## Evidence

URL design [9], variants [10], merchant listing [17], feed [18], facets [22]. Donor checklist [3] adapted; arbitrary scores, image/word thresholds and Shopping share as market share rejected. Full sources: [sources.md](sources.md).
