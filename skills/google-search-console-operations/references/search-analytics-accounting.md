# Search Analytics: pagination, totals and privacy

Verified against official docs on 2026-09-24. Recheck schema/docs when capabilities change.

## Request manifest

Save exact `site_url` returned by `list_sites`, inclusive start/end dates (PT for daily data), search type, ordered dimensions, filters, requested/returned aggregation, row limit/offset, response retrieval timestamp, wrapper/schema version and freshness. Country API filter uses ISO 3166-1 alpha-3; do not substitute a two-letter GA4 code.

Current exposed `mcp__gsc__search_analytics`: `site_url,start_date,end_date,dimensions,row_limit,start_row,search_type,dimension_filter_groups,aggregation_type`. Defaults: row_limit=100, start_row=0, search_type=web, aggregation_type=auto. Official API names are camelCase: rowLimit/startRow and `type` (deprecated searchType). Do not pass official parameter names to MCP without checking wrapper schema. This wrapper does not expose `dataState`; do not request hourly_all or claim explicit freshness control through it.

## Bounded extraction

- Get baseline totals without query/page dimensions or filters, retaining intended country/device/search-type filters and aggregation. If a page/query filter is necessary, label its limits instead of claiming complete totals.
- For detailed large exports, use one finalized day per request/query family with fixed dimensions/filters/aggregation; row_limit up to 25000 and start_row=0.
- Append each page to persistent artifact; advance by returned row count. Stop when returned count is less than requested, or when a next request returns zero. Detect repeated pages/non-progress, preserve original rows and reconcile unique dimension keys per day+query family. Conflicting duplicate rows require investigation, not summation.
- The official API exposes up to 50K rows/day/search type sorted by clicks. A short/empty page completes exposed rows, not all underlying search events. Ties have arbitrary ordering: freeze dates, note retrieval window and reject inconsistent overlapping exports.
- If offset isn't exposed in another installed wrapper, use an approved direct helper or UI export; date splitting alone cannot recover a truncated high-volume day. Do not call 100 returned rows 'all data'.

## Interpretation

Query/page detail can lose data for processing reasons; anonymized/rare queries are omitted. Query-filtered match+not-match totals need not equal unfiltered totals. UI table limit is 1000; charts and page-vs-property aggregates differ. Requesting `aggregation_type=byProperty` while grouping/filtering by page is invalid; use auto/byPage as supported. Do not mix aggregation types.

Calculate CTR = sum(clicks)/sum(impressions) for compatible disjoint rows. Impression-weighted position is a limited descriptive aggregate, not rank-tracker position. Do not average CTRs/positions naively, sum overlapping dimensions/periods, or rebuild top-level totals from truncated detail. Display clicks/impressions separately from visits/conversions; GSC and analytics differ by processing, privacy, JS/consent, time zones and delay.

Search Generative AI data is included within Web performance, so adding an AI native export to Web double-counts. A discovered searchAppearance value must be checked against documentation; do not invent an AI enum from the existence of an AI UI report.

## Official references

- https://developers.google.com/webmaster-tools/v1/searchanalytics/query — rowLimit 1–25000, zero-based startRow, dataState, type/aggregation rules; API does not guarantee all rows.
- https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data — daily queries, 50K rows/day/type, page/query data loss, searchAppearance two-step querying.
- https://support.google.com/webmasters/answer/17010575 — anonymized queries, table/chart discrepancies, PT and time lag.
