---
name: seo-content-operations
description: "Use when creating or improving SEO content."
version: 1.0.0
author: Hermes Agent
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [seo, content, editorial, fact-checking, refresh, cro]
    related_skills: [seo-aieo, seo-research-strategy, humanizer-ru, seo-site-architecture, technical-seo-audits, seo-specializations, aieo-visibility, seo-authority-promotion, seo-reporting-monitoring, google-search-console-operations, rank-tracker-operations, ga4-project-reporting]
---

# SEO Content Operations

## When to Use
Use for editorial briefs, articles and commercial pages, substantive editing, fact-checking, release preparation, content refresh/consolidation recommendations and conversion experiments. This owns the editorial loop under `seo-aieo`; it does not make an unreviewed draft safe to publish.

## Procedure
Load [editorial workflow](references/editorial-workflow.md) for production and release. Load [refresh and CRO](references/refresh-cro.md) for improvement work. Follow [data contracts](references/data-contracts.md). [Sources](references/sources.md) records donor ideas and rejected rules.

### 1. Select the page and outcome
- **Input:** `seo-research-strategy` brief/map, existing page or requested topic, audience, market/language, offer and voice examples.
- **Procedure:** recover project context; inspect current page and any overlap candidates. Establish the reader's task and one primary outcome. Review available performance data before deciding create/refresh/rewrite/merge-review/leave-alone. Separate language and market variants.
- **Output:** page record in [editorial-calendar.csv](templates/editorial-calendar.csv), source snapshot and selected scope.
- **Verification/stop:** if query ownership/intent is unresolved, request research/architecture review. Without accounts, make an evidence-based editorial assessment, not a claim of traffic decay or revenue upside.

### 2. Build a useful, verifiable brief
- **Input:** target page/intent, public sources and authorized first-party material.
- **Procedure:** complete [editorial brief](templates/editorial-brief.md). Define the answer, required evidence, what adds value beyond existing results, scope exclusions, section-level questions, CTA and reviewer. Fetch primary sources; identify missing research or demonstrations before drafting.
- **Output:** approved-for-drafting brief, evidence requests and [claims.csv](templates/claims.csv).
- **Verification/stop:** no credible distinct contribution means narrow scope, gather evidence, improve an existing page or defer. Do not manufacture interviews, testing, customer stories, statistics or author expertise. YMYL topics require suitable expert review before release.

### 3. Draft and prepare on-page elements
- **Input:** brief, verified evidence and brand voice examples.
- **Procedure:** answer the reader's task; support factual passages with claim IDs and citations. Create the draft, title/H1/meta description, proposed internal links, relevant CTA and asset/alt-text notes. Use `humanizer-ru` for clarity while preserving facts and local punctuation.
- **Output:** versioned local draft, metadata/link proposal and updated claim ledger.
- **Verification/stop:** no fixed word counts, keyword density, mandatory paragraph lengths or invented personal experience. Use natural terminology, not an LSI keyword quota. Unsupported central claims block review readiness.

### 4. Review facts, usefulness and conversion path
- **Input:** draft, claims, source snapshots and acceptance criteria.
- **Procedure:** review structure/task completion, fact accuracy/currentness, permissions, attribution, originality, market suitability, accessibility and offer/CTA truth. Reopen the underlying evidence rather than trusting a previous AI summary. Have the named author approve the actual final version; record expert/legal approval where needed.
- **Output:** reviewed draft with resolved changes, blocked claims or explicit exclusions; approval tied to version/hash in [release packet](templates/release-packet.md).
- **Verification/stop:** substantive edits invalidate relevant approvals. No fake bylines, credentials, testimonials or guaranteed outcomes. SEO check completion never substitutes for fact-check/author/YMYL approval.

### 5. Prepare and verify release
- **Input:** approved version, exact destination, intended CMS status, metadata and rollback plan.
- **Procedure:** default to local preview. Show the full material change and exact target/status; obtain user confirmation before ANY external CMS write, publish, send or distribution. With authorized access, explicitly set all relevant status fields, then read back the exact record and rendered target. Route technical/schema/index checks to `technical-seo-audits`.
- **Output:** release packet, remote ID/URL/status and verification evidence, or an upload-ready local package with the blocker stated.
- **Verification/stop:** no access or approval means no external action. Success response alone is insufficient; status/body/version mismatch stops further writes. A draft is not published; a live URL is not proof of indexing, rankings or AI citations.

### 6. Refresh without erasing useful evidence
- **Input:** content inventory, current facts and comparable query/page/performance observations.
- **Procedure:** diagnose factual staleness, changed intent, technical issues, demand shifts, snippets and conversion separately. Follow [refresh and CRO](references/refresh-cro.md); preserve useful material and URL where appropriate. Send suspected overlap to research/architecture before consolidation. Record before/after and re-run affected reviews.
- **Output:** [improvement plan](templates/improvement-plan.md), revised draft and change log, measurement window and rollback criteria.
- **Verification/stop:** no automatic deletion for low traffic, no cosmetic date bump, no full rewrite solely for a score. Redirects/removals require separate approved implementation and readback.

### 7. Test and learn
- **Input:** verified instrumentation, baseline, hypothesis, eligible traffic and business goal.
- **Procedure:** design a bounded CTA/offer/message/structure experiment with unit of analysis, denominator, primary metric, guardrails and stop rule. Have `ga4-project-reporting`/`seo-reporting-monitoring` verify events and analyze comparable cohorts; keep GSC/rank/AI outcomes distinct.
- **Output:** experiment section of improvement plan, measured result or `inconclusive`, decision and next review date. Hand authorized promotion drafts to `seo-authority-promotion`.
- **Verification/stop:** no uplift claims from before/after alone; no assumed sample size, fabricated baseline or repeated peeking for a winner. Low traffic supports qualitative usability evidence, not a statistically proven lift.

## Pitfalls
- Turning competitor headings into an outline without a reader task or evidence advantage.
- Mistaking citations for fact-checking: a real URL can fail to support the nearby claim.
- Using AI-detector scores or synthetic E-E-A-T scores as acceptance tests.
- Removing navigation, adding urgency, or changing CTAs universally without context or truthful offer terms.
- Treating a CMS draft save as a harmless local edit. It is an external write and needs preview, confirmation and readback.
- Promising rich results or AI citations from content structure/schema. Delegate eligibility and measured visibility to the appropriate specialist.

## Verification
Before handoff, parse calendar/claim CSVs, resolve page/claim IDs and provenance, check unresolved placeholders, verify the exact approved version and confirm all blocking claims/reviews. Return artifact paths, status, approvals missing and measurable next step. No publishing happened unless verified readback proves the requested external state.
