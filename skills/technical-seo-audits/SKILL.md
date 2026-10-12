---
name: technical-seo-audits
description: "Технический SEO-аудит: индексация, canonical, robots, редиректы, hreflang, схемы, Core Web Vitals, JavaScript-рендеринг, логи, миграции, Яндекс. Использовать, когда просят «проверь индексацию», «технический аудит сайта», «почему страница не в индексе», «проверь canonical и редиректы», «разбери падение после миграции»."
version: 2.0.0
author: Sirenko SEO/AIEO Skills contributors
license: MIT
metadata:
  seo:
    tags: [seo, technical-audit, indexing, schema, cwv, migrations]
    related_skills: [seo-site-architecture, google-search-console-operations, seo-specializations, seo-reporting-monitoring]
---

# Technical SEO Audits

## When to Use

Use for technical audits, crawl/index discrepancies, robots/canonical/schema, CWV/JS/log diagnosis, migrations and incident recovery. For site design rather than diagnosis, route to `seo-site-architecture`.

## Contract

Input: exact domains/properties, engines, business-critical URLs, scope (page/template/site/migration/incident), permissions, available exports, and request/time budget. Resolve domain mistakes before crawling. Default to read-only. If only saved HTML is available, do an **offline observation review**, not a live-site audit.

Output: scope/coverage ledger, page inventory, evidence-linked findings, dependency-aware fixes with acceptance tests, unknowns, and verification plan. A “full audit” covers all relevant categories, not every URL; explicitly mark sampled, unavailable and untested areas. Use `templates/audit-evidence.md`.

## Workflow

1. **Inventory access and budget.** Set limits before fetching. Load `references/public-full-site-audit-playbook.md` for any live crawl or full audit. No automatic dependency installation, private/internal hosts, paid calls or unbounded recursive crawl.
2. **Observe HTTP and discovery.** Record redirects, GET status, headers, robots and recursive sitemap evidence; compare bounded raw-HTML and rendered samples. A sitemap declaration absent from robots is a discovery improvement, not an automatic error.
3. **Separate states.** Discovered → fetched → renderable → index-eligible signals → engine-selected canonical/index state → ranked/traffic are different observations. `200`, crawl logs, sitemap inclusion, self-canonical or `index,follow` do not prove indexing. `site:` is not a census. GSC/Webmaster data requires correct property, dates and actual access.
4. **Diagnose by template.** Sample home, hubs, detail, languages, pagination/facets, recent/changed, important and anomalous URLs. Compare raw/rendered metadata, links, content and mobile parity. State denominators before generalizing.
5. **Deep checks.** Load `references/schema-cwv-js-logs.md` for structured data, field/lab performance, rendering or logs. Load `references/migrations-incidents.md` for moves, deindexing or traffic-drop recovery. For Yandex, also load `references/yandex-technical-audit.md`; route regional/content work to `seo-specializations`.
6. **Prioritize evidence, not a fixed checklist order.** Rank confirmed impact on critical pages × extent × confidence, with dependencies, effort and reversal risk. Security/outages may outrank links; an intentional noindex is not a defect. Missing descriptions or multiple H1s are review signals, not universal indexing blockers.
7. **Implement only within approved scope.** Robots/canonical changes, redirects, production deployment, sitemap submissions, indexing requests, IndexNow, console moves, Metrica linking and monitoring creation are external writes: obtain explicit approval, then read back exact targets. Never claim approval or deployment from a proposed diff.
8. **Verify.** Retest original failures on staging and, after approved deployment, production. Keep technical recovery, observed recrawl, index recovery and performance recovery separate; they occur on different timelines. Hand ongoing measurement to `seo-reporting-monitoring`.

## Offline HTML evidence utility

Load `references/offline-html-checker.md` before use. The skill directory is the directory this SKILL.md was loaded from (when installed as a plugin: `skills/technical-seo-audits/` inside the plugin directory); do not assume another profile or donor plugin path.

```bash
python3 <skill_dir>/scripts/html_evidence.py --html /path/page.html --url https://example.com/page --out /path/new-evidence.json
python3 -m unittest discover -s <skill_dir>/scripts -p 'test_html_evidence.py' -v
```

Python stdlib only. No HTML execution, network or link fetches. Preserves duplicate tags, metadata, title/H1, robots tokens, canonical/hreflang, base-aware observed links, JSON-LD parse results. It is **not a crawler**, DOM engine, schema validator, index/rank checker or mobile-speed test.

## References

- `references/public-full-site-audit-playbook.md` — bounded collection, sitemap safety, coverage, CMS and public checks.
- `references/schema-cwv-js-logs.md` — technical interpretation and current official sources.
- `references/migrations-incidents.md` and `templates/migration-map.csv` — mapping, rollback, acceptance and recovery.
- `references/offline-html-checker.md` — CLI guarantees, limits and tests.
- `references/yandex-technical-audit.md` — engine-specific technical extension (not duplicated).
- `references/source-adaptation.md` — pinned donors, adopted concepts and rejected assumptions.

Architecture decisions (intent→URL, linking, programmatic rollout) belong to `seo-site-architecture`; technical checks validate that design rather than inventing business demand.
