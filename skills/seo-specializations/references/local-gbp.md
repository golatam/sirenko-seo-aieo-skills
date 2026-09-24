# Local SEO / Google Business Profile

## Input → output → validation

**Input:** business legal/trading identity, GBP URL/ID, website, actual premises/service areas, opening hours, branch/practitioner roster, proof of real operation, target languages, read-only exports and conversion definition.
**Output:** location/entity register, GBP↔site↔directory discrepancy table, page briefs, review-response/request DRAFTs, approved changeset and measurement plan.
**Validation:** eligibility before optimization; proof for factual fields; no fake office, no review manipulation; profile/page corrections read back individually. Use [local-audit.md](../templates/local-audit.md).

## 1. Eligibility and reality gate

Classify each entity `storefront`, `service-area business (SAB)`, `hybrid`, `practitioner/department`, `ineligible/unclear` based on real operations, not a Maps embed.
Google requires accurate real-world representation/address or service area. A mailing-only virtual office is not eligible; coworking needs signage, customer reception and the business's own staff during stated hours.[6]
For SAB without customer-facing premises, do not expose a private home address merely for NAP consistency. Confirm current address-hiding/service-area rules and operation with owner. A service area does not create an eligible separate office/profile in every city.[6]
Special branches/practitioners/departments need the current category-specific rules; do not create duplicates by default. Online-only/ineligible businesses → organic route, not fabricated GBP.
**Stop:** ownership unclear, business not operating, fake/borrowed address, request to evade suspension; propose factual evidence/reinstatement review, not a new duplicate profile.

## 2. Build canonical facts register

For each location record stable business/location ID, public name, authorized public address or hidden status, phone, site/location URL, primary activity, categories, regular/special hours, services, accessibility, appointment/menu/order URLs, factual proof and checked_at.
Resolve conflicts with business owner and authoritative operation records. User-facing facts and legal entity names can differ; preserve the legitimate trading identity, not automatic legal-name replacement.
Choose the fewest accurate categories describing the core activity, not keyword categories. Name follows real-world branding; do not add city/service/ranking keywords as a trick.[6]
Credentials/signage/lease material can be sensitive: retain only proof reference/status, never publish raw documents or private address.

## 3. Read-only baseline and discrepancy audit

1. Read exact GBP/public listing and authorized export if available; website alone cannot show GBP management state.
2. Compare visible site content, structured data, GBP and selected legitimate local/vertical directories for name, public address policy, phone, hours and URL.
3. Separate harmless formatting/local language variants from substantive mismatches (wrong branch, phone, closure, hours, redirect).
4. Note duplicate/suspended/unverified status only from actual evidence; never promise reinstatement.
5. Sample markets by named query, map/search surface, precise location, language, device and date. Position is contextual, not a universal local rank. Do not run unauthorized bulk Google scraping.
6. Record actual website leads/calls/bookings and any available GBP metrics with definitions; direction request/call-click is not a verified store visit or completed call.

## 4. Useful service/location pages

Inventory store locator, crawlable location pages and actual services. A location page must help someone choose/reach/use that location: real staff/offer, hours, service constraints, directions/accessibility, licensed original photos, contact and relevant local proof.
For SAB, explain verified area/availability without claiming nonexistent premises. Create a city-specific service page only where intent and distinct useful local facts justify it; otherwise a strong service-area hub. No quotas or arbitrary uniqueness percentage.
Branches may share policy text; city-name swapping without real local value is a doorway risk, not an automatic numerical verdict. Link service↔location↔contact coherently; use `seo-site-architecture` for implementation.
Structured data must match visible facts and the entity. Choose accurate Schema.org type; separately verify Google's current supported feature/required properties. Do not invent an address for markup, or assume on-site self-serving business reviews qualify for review stars. Missing unsupported markup is not a business-critical error.

## 5. Reviews and reputation

Google prohibits incentives, fake/conflicted reviews and selectively soliciting positive reviews; requests must not dictate a rating/content.[7]
- Analyze genuine themes and dates; distinguish public snapshot from full history. No «18-day ranking cliff», minimum-star magic number or review quota.
- Draft neutral request after an actual customer interaction, without satisfaction gate, rewards, prescribed keywords or pressure. External send needs approval.
- Read the review/context before response; draft concise factual help. Never reveal health, legal, financial or customer records or confirm a sensitive relationship publicly.
- Negative review ≠ fake review. Flag only documented policy violations, not criticism; report/removal request is an external action requiring confirmation/read-back.
- Do not ask employees/family/agencies for customer reviews, fabricate owner responses, or offer compensation to revise/remove a review.

## 6. Vertical adaptations

| Vertical | Additional input | Validation/limits |
|---|---|---|
| Restaurant/hospitality | Current menu, booking, accessibility, seasonal hours | Correct location/menu/prices, food claims reviewed; photos licensed |
| Home/mobile services | Real service radius, travel fees, emergency capacity | No fake offices, no 24/7 claim without delivery capacity |
| Medical/legal/finance | Practitioner eligibility, credential sources, local ad/privacy review | No guarantees; sensitive-review replies stay non-identifying |
| Retail/dealership | Store inventory/department IDs, pickup terms | Local availability matches actual stock; combine commerce module |
| Real estate/franchise/multi-location | Agent vs office identity, brand rules, real branch roster | No listing-address offices; entity/profile eligibility checked separately |
| Education/nonprofit/B2B | Public-facing operations and appointment rules | Do not assume eligibility merely from legal registration |

## 7. Change gate and pilot

Changeset includes location/profile ID, old/new field, source, risk (e.g. reverification), owner approval, rollback and exact verification test. Do not claim/merge/delete profiles, edit hours, publish posts/photos, request reviews or buy memberships without approval.
After allowed write reread exact profile field and public state; pending/reviewed/published differ. Reverification or rejected changes → hold, not repeated automated edits. Web changes separately read rendered page + schema.

## 8. Measurement and completion

Compare stable query/geo strata and periods; separate local pack, organic, GBP actions, website leads and actual revenue. Keep source scope/call tracking/consent caveats. `seo-authority-promotion` handles legitimate citations/community PR, not purchased ranking signals.
Report verified discrepancies/fixes, unknowns, next owner/date. Eligibility/completeness does not guarantee local rank; proximity and observed demand vary.

## Evidence

Official representation [6], review policy [7]; donor local audit dimensions [2] adapted, numerical ranking weights/review cadence/AI conversion assertions rejected. See [sources.md](sources.md).
