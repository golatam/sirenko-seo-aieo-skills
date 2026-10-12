# Editorial production and release procedure

## Intake and editorial decision

Input: page map or topic, current page/snapshot, reader, market/language, offer, business event and voice examples. Read relevant project notes before asking for information already stored. If no query map exists, inspect likely existing pages and label the topic provisional; do not silently create another page targeting the same job.

Procedure: establish what a reader should know or accomplish after the page, why this project can credibly help, what is commercially appropriate next, and whether current content already solves it. Review page type, customer stage and production/review capacity. Choose create, refresh, rewrite, merge-review or leave-alone with evidence. Do not let a blanket publishing quota override this choice.

Output: page ID, current/proposed URL, lane, owner, scope and a calendar row. Verification/stop: if the offer cannot be delivered, the claim requires unavailable expertise, or the target conflicts with another page, block release planning and assign the missing evidence/decision.

## Evidence-first brief

A usable brief is an argument plan, not a list of keywords. Each proposed section must name the user question, intended answer and supporting asset/claim. The introduction should resolve or orient the main task before unnecessary background. Include limitations, alternatives and who the solution is not for.

Require a specific useful contribution beyond restating the SERP, for example:
- A documented workflow tested in the user's real product, with version, conditions and test record.
- An original analysis of a public dataset, with the dataset, calculations, inclusion criteria and limitations saved.
- A sourced local/jurisdictional comparison that explains differences relevant to the buyer.
- A worked example using disclosed assumptions, clearly labeled as an example rather than a customer result.
- An expert-reviewed decision tree with applicability boundaries.
- An authorized first-party case with actual measurements, permission and the possibility of confounding stated.

These are options, not quotas. Never invent testing or an expert quotation to satisfy the brief. If evidence is unavailable, use a narrower well-supported answer or deliver the brief/evidence request as the partial artifact.

For comparisons: define the alternatives and selection criteria before writing the verdict. Check current prices/features on official pages; name date, currency, tax, period, plan and exclusions when relevant. Explain affiliation and use consistent criteria. Do not manufacture an independent review of the user's own product or imply hands-on experience from reading documentation.

For how-to pages: verify prerequisites, sequence, exact commands if included, failure cases, reversibility and completion evidence. If not executed, label as documentation-based instructions, not a tested tutorial. For commercial pages: substantiate promise, eligibility, price, next step, delivery conditions and proof; no fabricated scarcity or guarantees.

## Claim ledger and fact check

Extract atomic material claims: numbers, results, dates, availability, product capabilities, comparisons, quotations, safety/legal advice, credentials and causal claims. Store exact draft text, source locator, status, market/language, dates and reviewer in claims.csv. Separate facts from opinions and illustrative assumptions.

For each factual claim:
1. Open the primary source using page fetch / file read tools or browser as appropriate. Capture the relevant passage/table/row and retrieval time; snippets and generated summaries are discovery aids.
2. Check entity, date, geography, product/version, units, population/denominator and whether the source supports the exact wording. Recalculate derived numbers with tools and store formula/inputs.
3. Distinguish a vendor claim from independently observed evidence. Seek corroboration for consequential disputed claims and retain contradictions.
4. Preserve attribution and quotation accuracy. Keep necessary caveats next to the claim; a source in a footer does not license stronger wording.
5. Mark supported, needs verification, contradicted, removed or qualified. Unsupported central claims block release; softer wording is allowed only when it accurately expresses the source's uncertainty.

For sensitive customer data, keep only necessary anonymized evidence in the deliverable and protect the underlying file. Check consent before publishing quotations, names, screenshots, logos or personal data. Document asset rights; existence online is not permission to reuse.

YMYL: identify health, safety, finance, legal or other high-consequence advice in the brief. Require an appropriate qualified human reviewer for the relevant jurisdiction/topic. Record scope of review and exact draft version. Do not invent a reviewer or credentials. A disclaimer is not a replacement for competent review, and a general source does not establish individual eligibility/advice.

## Draft and on-page package

Write to satisfy the task, not a length/density score. Match language, terminology and register to the audience; avoid translations that import another country's facts. Give complete answers without redundant boilerplate. Sources support factual sections; practical examples explain application.

Prepare separately:
- Accurate title/H1 and description with the actual value/limitations of the page. Length is a display concern, not a fixed ranking threshold; preview likely truncation rather than promise an exact snippet.
- Proposed URL and page ID; do not change an existing URL casually.
- Internal links with source page, target URL, descriptive anchor, reader benefit and target existence/status. No forced exact-match anchors or links to unverified proposed URLs.
- External citations near the supported assertions.
- Visual/asset requirements, rights and meaningful alt text. Decorative images should not receive keyword-stuffed descriptions.
- Contextual CTA and truthful next-step expectations. On informational pages, do not withhold the answer merely to force conversion.
- Author/reviewer identity only when real and approved. Explain method/automation where material to trust or required by policy.

Structured-data and indexability implementation belongs to the technical owner; proposed content must match visible facts. No markup guarantees rich results or AI inclusion. Answer clarity is useful editorial practice, not proof of AI citation lift.

## Review gates

Use separate passes because a fluent draft can hide unsupported claims:
1. **Task/structure:** reader can answer the primary question or complete the process; limitations and alternatives are clear.
2. **Evidence:** every consequential factual claim has sufficient support; numbers, quotations and source dates checked.
3. **Original contribution:** actual useful evidence or analysis present; no plagiarism or lightly rewritten competitor copy.
4. **Language/voice:** apply humanizer-ru while preserving technical/legal meaning and local punctuation; never add invented anecdotes.
5. **UX/accessibility:** meaningful headings, readable tables, link purpose, image alt text and truthful CTA. Text-only review cannot prove layout/mobile behavior; record the limitation or inspect a real preview.
6. **Accountability:** named author approves the final version, reviewer/legal approvals completed for their scope, unresolved issues assigned.

No AI-detector percentage, word count or vendor SEO score can pass these gates. Track revisions; significant new facts or offer changes reopen their approvals. Keep author/editor/reviewer roles honest if one human fills several roles.

## Release contract

Input: reviewed local package, current version/hash, target account/site/record, requested status and rollback owner. The default is local draft only. Use `write_file` for local artifacts and retain the user's existing text unless the edit scope authorizes replacement.

Before an external write:
1. Show a preview/diff of the actual content, metadata, destination, intended visibility/status, schedule/timezone if any, authorship, media, links and affected records. Show rollback implications.
2. Obtain explicit user confirmation for that exact scope. Do not treat author editorial approval as permission to publish. A changed payload/target requires renewed confirmation.
3. Discover the live connector/browser capabilities; never invent a WordPress or CMS command. Set status explicitly (`draft` if authorized only for draft), not by provider default. Never expose or type secrets outside approved credential tools.
4. Execute only the approved action. Read back the exact remote ID and fields; for a public release also fetch/render the public target. Verify body/version, status, canonical target, metadata and schedule. Do not submit live forms or test purchases without separate authorization.
5. Save readback evidence. If mismatch or access failure occurs, stop, report actual state and prepare an approved correction/rollback. Do not claim published from an HTTP success or silently retry an ambiguous create (risk of duplicates).

Output statuses: `local_draft`, `review_blocked`, `ready_for_confirmation`, `external_draft_verified`, `published_verified`, `verification_failed`. Only use the final two success states with exact readback. Live delivery, indexing, ranking, conversion and AI citation are distinct observations.

Handoff to monitoring includes page/query IDs, release timestamp, change scope, country/language, baseline period, event definition, reviewer and known confounders. Promotion material goes to seo-authority-promotion as a draft; no distribution happens by implication.
