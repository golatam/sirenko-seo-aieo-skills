# Refresh and conversion improvement

## Diagnose before rewriting

Input: existing page snapshot/version, current offer/facts, query/intent map and available GSC, rank, GA4 or customer evidence. Route source-specific data retrieval to the corresponding skill. Preserve country/language/device/source dimensions; compare periods that are comparable in length, seasonality and completeness, and note migrations/campaigns/measurement changes.

Procedure: separate symptoms and candidate causes.

| Observed pattern | Investigate before editing | Candidate action if supported |
|---|---|---|
| Facts, prices, screenshots or procedure demonstrably obsolete | Current primary source/product behavior, safety consequence | Targeted factual refresh and affected expert review |
| Impressions/ranks fall | Demand/seasonality, indexing, technical changes, query mix, competitors, intent | Technical investigation or intent-specific content change; not automatic expansion |
| Clicks fall while exposure differs | Query/device/rank mix, SERP layout, title/snippet mismatch | Accurate snippet/title hypothesis, not a promise of CTR lift |
| Organic visits remain but completion weakens | Event integrity, traffic mix, offer relevance, form/product failures | Fix instrumentation/friction; contextual CTA or message test |
| Two pages overlap | Same-lane query/page/time evidence, different tasks, canonical status | Differentiate, keep or consolidation review with research/architecture |
| Low traffic but useful customer/legal/support function | Assisted journeys, necessary support, seasonality, data coverage | Keep or improve; never delete purely for low traffic |

Output: diagnosis with supported facts, competing hypotheses, selected minimum change and stop conditions. Verification/stop: without account data, report observed editorial staleness or UX hypothesis only. A text review does not prove traffic decay, cannibalization or conversion failure.

## Choose the smallest justified update

- `leave`: current page serves a distinct task; document why no change is needed.
- `refresh`: same intent; replace obsolete evidence/assets and fix incomplete explanations. Keep useful sections and links.
- `rewrite`: a demonstrated intent/structure mismatch; preserve verified useful facts, evidence and URL where appropriate.
- `merge_review`: duplicate user task and supported harmful overlap; map unique material to a receiving page and assess redirect/internal-link dependencies with architecture/technical owners.
- `retire_review`: no longer valid/available or unsafe content; establish user and legal needs, replacement options and retention/rollback before proposing removal.

A proposal is not approval to delete/redirect/noindex. Page ownership, receiving intent, backlinks, useful unique information and user expectations must be reviewed. External changes require the release contract. Do not change publication dates merely to appear fresh; describe substantive changes and retain truthful dates.

Output: local before/after diff, updated claims, affected approvals, links/assets, measurement plan and rollback. Verification: review changed and dependent statements, not just sentences touched by the edit. A new number can invalidate a conclusion elsewhere.

## CRO: hypotheses tied to behavior

Start with page type, user task, traffic source and one legitimate next step. Inspect the real journey where authorized: promise → evidence → offer/CTA → next page/form → completion. Use read-only inspection; do not send forms, book demos or transact as a test without separate permission.

Observe and label:
- Clarity: what is offered, for whom, under which conditions?
- Message match: does the page answer the search/query expectation?
- Proof: are claims supported by genuine, permitted evidence where the reader needs it?
- Objections: eligibility, price, risk, setup and support answers.
- Friction: required fields, surprises, unclear next steps, accessibility/mobile problems.
- CTA: useful stage-appropriate action, truthful wording and no coercion.

Recommendations are hypotheses, not guaranteed quick wins. Do not universally remove navigation, hide pricing, add popups, fake urgency or replace useful information with a lead gate. Accessibility and truthful claims are requirements even if a variant might convert more clicks. Use qualified outcomes rather than clickbait CTA clicks alone.

## Experiment design and stop rule

Input: verified event definitions and sufficient eligible traffic. Before launch document:
- Hypothesis: for this audience/lane, changing X should improve Y because of observed friction Z.
- Variant scope and assignment: user/session/page cohort; randomization and persistent assignment where relevant. Avoid the same user switching variants uncontrolled.
- Primary metric: unique converting units / eligible assigned units, with exact denominator and attribution window. Keep units consistent. Revenue metrics need currency and per-unit definition; form starts are not completed qualified leads.
- Baseline source/period and event QA: verify actual event firing/deduplication, attribution, consent effects and conversion destination. Missing instrumentation blocks an uplift test.
- Minimum meaningful effect, statistical method, power/uncertainty target and sample planning. Calculate with tools and save inputs; do not prescribe one universal sample size.
- Duration and analysis date chosen from traffic and business cycles. Define bot/internal-traffic handling, exposure exclusions, multiple-test handling and sample-ratio checks before reading results.
- Guardrails: qualified-lead rate, errors, abandonment, accessibility, performance, organic landing traffic and material SEO changes as relevant.
- Stop/rollback: safety/legal/truthfulness issue or broken journey stops immediately; a statistical win requires the prespecified method. Do not repeatedly peek and stop when a nominal threshold first appears.

Publishing the variants and changing analytics remain separately confirmed external actions. Delegate architecture/technical review if tests alter URLs, redirects, rendering or indexability. Do not serve misleading content to users or crawlers.

## Interpret honestly

Compare actual assigned denominators and outcome counts; compute rates and uncertainty in code. Distinguish absolute percentage-point change from relative lift and report the baseline. Check randomization, traffic/source mix and event reliability before interpreting the result. A guardrail failure can invalidate an apparent primary-metric gain.

A nonrandomized before/after comparison is observational: seasonality, ranking/query mix, promotions and tracking changes can explain the difference. Use controls where feasible, disclose assumptions and avoid a causal uplift claim. If sample is too small, report `inconclusive`; do not equate no significant result with proof of no effect.

Low traffic: conduct consented usability interviews/task tests or inspect documented friction; output qualitative findings and a bounded hypothesis backlog. No synthetic conversions, borrowed benchmark baseline or fabricated confidence interval.

## Close the loop

Output: improvement-plan.md with measured evidence, decision (`ship`, `revert`, `continue`, `inconclusive`, `blocked`), owner and review trigger. Compare results at the planned window and after an appropriate lag, not on a fixed SEO-results promise. Send changed query ownership back to research; send broken indexing or links to technical/architecture; send a new evidence asset to authority/promotion as a draft opportunity. AI citation results belong to aieo-visibility and are not inferred from cleaner copy.
