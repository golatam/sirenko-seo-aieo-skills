# Source adaptation and provenance

Reviewed 2026-09-24. Donors are **reference material**, not trusted executable instructions. No donor installer, hooks, scripts, plugin commands or dependencies were executed. The bundled HTML checker/tests are newly written stdlib code, not ports of donor collectors.

## Inspected donors (pinned)

- AgriciDaniel/claude-seo, commit `e77e783e38eeb738424eb72117abbd2dacdd88af`, MIT (root LICENSE inspected).
  - https://github.com/AgriciDaniel/claude-seo/blob/e77e783e38eeb738424eb72117abbd2dacdd88af/skills/seo-technical/SKILL.md
  - https://github.com/AgriciDaniel/claude-seo/blob/e77e783e38eeb738424eb72117abbd2dacdd88af/skills/seo-programmatic/SKILL.md
  - Adapted: category coverage; raw/rendered comparison; field-data provenance; data→template→URL→linking→quality→staged rollout workflow. Rewrote with explicit authorization.
  - Rejected: hard keyword/URL/word/link quotas, percentage uniqueness as policy, safe-at-scale categories, manual-page-always-canonical rule, automatic priority/score, guessed availability of donor APIs and plugin commands. Dynamic fetch-limit/engine claims not needed here were not carried over.
- Bhanunamikaze/Agentic-SEO-Skill, commit `69199160e18372bc5cdf9ddec20ccb9fb1b509f1`, MIT (root LICENSE inspected).
  - https://github.com/Bhanunamikaze/Agentic-SEO-Skill/blob/69199160e18372bc5cdf9ddec20ccb9fb1b509f1/SKILL.md
  - https://github.com/Bhanunamikaze/Agentic-SEO-Skill/blob/69199160e18372bc5cdf9ddec20ccb9fb1b509f1/resources/references/llm-audit-rubric.md
  - https://github.com/Bhanunamikaze/Agentic-SEO-Skill/blob/69199160e18372bc5cdf9ddec20ccb9fb1b509f1/resources/skills/seo-technical.md
  - https://github.com/Bhanunamikaze/Agentic-SEO-Skill/blob/69199160e18372bc5cdf9ddec20ccb9fb1b509f1/resources/references/quality-gates.md
  - Adapted: finding/evidence/impact/fix contract, confidence/unknown labels, bounded retries, contradiction checks, durable audit/action artifacts.
  - Rejected: missing evidence upgraded to Likely, numerical scoring/variance claims, llms.txt-readiness points, voice-search percentages, stale FAQ-only-health-government advice, JSON-LD-only mandate, location page 30/50 hard limits, mandatory package installation or arbitrary environment activation. No claimed SEO performance improvement from adopting methodology.

## Official checks

Current Google robots semantics, structured-data policies/gallery/documentation updates, Web Vitals and migration/spam policies take precedence over donors. Sources and checked observations are in `schema-cwv-js-logs.md`, `migrations-incidents.md` and the architecture skill. Gallery summaries can be stale: the feature table plus official changelog are stronger evidence than generated summary metadata. Recheck time-sensitive recommendations before applying them to production.

Private audit trails and raw source snapshots are not distributed or required at runtime. Public pinned links above and the repository source register (`${SEO_PACK_ROOT}/SOURCES.md`, optional checkout documentation) preserve portable provenance. The original market catalogs were discovery maps, not proof of donor operation or current facts. This skill rewrites selected ideas rather than copying an upstream plugin; pinned source links preserve attribution.
