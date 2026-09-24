# Technical audit — <project / date / run_id>

## Scope and access
- Exact origins/properties, engines, purpose, requested coverage:
- Data sources/access actually verified; dates/timezones; missing sources:
- Mode: live HTTP / rendered / authorized export / offline saved HTML:
- Approved limits: URLs, HTTP requests, renders/subresources, hosts, seconds, bytes, sitemap depth/files/entries:
- Safety/robots/rate-limit policy; tools and versions:

## Coverage (compute, do not estimate from memory)
| Source/template | Known universe or unknown | Discovered unique | Attempted | Fetched | Rendered | Failed/skipped | Frontier/stop reason |
|---|---|---|---|---|---|---|---|

## Page inventory
| URL | Source/template | Timestamp | HTTP/final URL | Robots header/meta | Canonical | Raw/rendered | Artifact | Untested |
|---|---|---|---|---|---|---|---|---|

## Findings
| ID | Fact / hypothesis | Severity | Confidence | URL/cohort + observed/denominator | Exact evidence + artifact/date | Expected impact (not promise) | Fix | Dependency/effort | Owner | Acceptance/recheck |
|---|---|---|---|---|---|---|---|---|---|---|

Status vocabulary: observed / likely / hypothesis / unavailable / not-tested. Multiple URLs with same template cause are one finding with a measured extent, not inflated duplicate issues. Contradictory evidence remains visible until resolved.

## Approval and verification
- Read-only recommendations vs explicitly approved writes:
- Staging test result:
- Production readback of exact targets:
- Console state/recrawl/index recovery (independent of HTTP recovery):
- Follow-up date/owner, unknowns and requested exports:

## Summary
Confirmed business-critical issues first; no invented audit score, rankings, traffic, CWV or guarantees. List artifact paths and coverage limitations.
