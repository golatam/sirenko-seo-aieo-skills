# Editorial artifact contracts (v1)

Use a project/run directory, not the skill folder. UTF-8 CSV with one header and proper quoting; blank means unknown. Dates: YYYY-MM-DD; timestamps: ISO-8601 with timezone. IDs are stable strings. Templates are intentionally empty and are not a completed project.

## editorial-calendar.csv

One work item per page/market/language/revision. Required: item_id, page_id, market, language, action, priority, owner, status, dependency, source_url_or_file, source_locator, updated_at. `owner=unassigned` is allowed only with a blocked/planned status. `dependency=none` must be explicit when there is none.

`action`: `create|refresh|rewrite|merge_review|retire_review|leave`.
`priority`: `now|next|later|blocked`.
`status`: `planned|research_blocked|brief_ready|drafting|review_blocked|reviewed|ready_for_confirmation|external_draft_verified|published_verified|verification_failed|measuring|closed`.

Target URL can be blank while planned/blocked but is required before external action. `query_map_ids` is semicolon-separated IDs from research mapping; blank is allowed only with provisional/unmapped explanation in dependency. `evidence_asset` and `brief_path` name actual files/assets by drafting; do not fill them with promised nonexistent assets. Due/review dates are commitments only when an owner confirms them, otherwise blank. `approval_ref` points to the exact release packet/version; external success states require populated approval_ref and release_readback_ref. Status is a record of verified state, not a wish.

## claims.csv

One atomic material assertion per draft version. Required: claim_id, page_id, draft_version, market, language, claim_text, claim_type, evidence_status, source_url_or_file, source_locator, checked_at, limitation. For unresolved claims, source locator can name the evidence request and checked_at the triage time; never invent a source URL. `limitation=none` must be deliberate, not a default.

`claim_type`: `fact|vendor_claim|quotation|calculation|opinion|illustrative_assumption`.
`evidence_status`: `needs_verification|supported|qualified|contradicted|removed`.

A supported factual claim needs actual source evidence and checked_at. A qualified claim needs draft wording that reflects the source limitation. Numeric claims fill `value`, `unit`, `period_or_asof`; currencies, percentages (ratio vs percent), population and denominator must be explicit. Derived calculations also require `calculation_record`. Non-numeric claims leave those numeric columns blank. Reviewer and approval_ref must name actual review, never generated credentials. Private source paths should be included only in authorized internal artifacts; published citations require an appropriate accessible reference or honest evidence description.

YMYL/expert approval is documented in the brief/release packet at the page/version scope, plus claim-specific references where needed. An author's approval is not scientific proof. A citation URL's presence is not a support verdict.

## Link and approval checks

1. Parse CSVs with `csv.DictReader`; compare header order against templates, detect malformed quoting/extra cells, blank required fields and duplicate IDs in code. Report empty templates explicitly.
2. Check page IDs, market/language and draft versions across calendar, brief, claims and release. A stale approval cannot authorize a changed version.
3. Verify local source/brief/approval files exist and external citations resolve through an allowed fetch method. A blocked source is a limitation, not proof it is dead.
4. Review all material claims in the draft against ledger coverage. Unresolved central assertions, contradictions or missing applicable expert/author approval block release. Remove claims only in the draft as well as the ledger.
5. Check unresolved placeholders, asset rights, proposed vs existing link targets, truthful metadata/offer and actual rendered preview coverage.
6. For any external success state, inspect the release packet: exact target, version, confirmation evidence, explicit status and readback evidence. Read the target again after a new external change. Internal file writes already verified by tools need no ceremonial readback.
7. Save actual validation counts and unresolved gates. Do not equate parse success with editorial quality, factual truth or permission to publish.

## Versioning and handoffs

Keep pre-edit snapshot, draft version, reviewed version and release version distinct. Hashes must be calculated with tools, never fabricated. A hash binds approval to bytes; it does not prove factual accuracy. Save substantive diff and rollback ownership. Research receives changed intent/query ownership; technical gets metadata/link/schema/index requirements; monitoring gets page IDs, real release timestamp, event definitions and baseline scope; promotion receives draft assets only until separately approved.
