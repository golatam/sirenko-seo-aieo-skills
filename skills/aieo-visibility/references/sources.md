# Sources, donor provenance and rejected claims

Verified review: 2026-09-24. Official product docs were retrieved/read; no donor installer/code executed and no paid/model API calls. This skill's implementation is independently written; methodological ideas adapted, not vendor code copied. No inter-model verification was run.

## Official primary sources

- Google guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — 'there's no special schema.org markup you need to add'; llms.txt ignored for Google Search visibility; index/snippet eligibility and included Search generative AI control. Scope: Google, not universal AI behavior.
- GSC Search AI help: https://support.google.com/webmasters/answer/16984139 — impressions, Pages/Countries/Dates/Devices, chart/table export, exported unavailable values become zeros; rollout note vs residual not-seeing-report wording. Capability confirmed, account access not tested here.
- GSC control: https://support.google.com/webmasters/answer/16908024 — include/exclude/inherit, default include and parent inheritance; not training control. Read-only check; no change performed.
- GSC Discover AI: https://support.google.com/webmasters/answer/16983858 — separate report/export, page aggregation; list portions of extraction incomplete.
- Launch: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports — separate Search/Discover impressions and Devices for Search.
- API: https://developers.google.com/webmaster-tools/v1/searchanalytics/query — rowLimit/startRow, dataState, supported types; no dedicated generative type shown in retrieved schema.
- API data limits: https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data — 50K/day/type, query/page-detail loss; no universal completeness.
- Privacy: https://support.google.com/webmasters/answer/17010575 — rare query suppression, UI limit, aggregation, PT.
- Bing launch: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview — citations, average cited pages, sampled grounding phrases, URL/time trends; not rank/authority.
- Bing update: https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare — globally rolling preview, four capabilities, query-level citation share denominator and limitations.
- Bing help: https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c — shell/sign-in only; dynamic browser read blocked by runtime browser-profile configuration. Native AI export/API details remain unverified, not asserted absent.
- OpenAI: https://developers.openai.com/api/docs/bots — independent search/training controls; ChatGPT-User distinct.

## Read donor files at pinned GitHub commits

1. `promptwatch-com/skills`, commit `36fb1231174bef63980f260500a9dbd1dd0ff18d`, repository license MIT (GitHub API metadata).
   - File: https://github.com/promptwatch-com/skills/blob/36fb1231174bef63980f260500a9dbd1dd0ff18d/skills/mcp/citation-deep-dive/SKILL.md
   - Adopted: owned-vs-third-party citations; per-engine/source/domain views; bounded same-period comparison; confirm collection before interpreting empty data.
   - Rejected: importing vendor tool names as available Hermes tools; causal 'likely reasons' without evidence; treating crawler attention as demonstrated citation probability; MCP install/config/key recipe.
2. `alirezarezvani/claude-skills`, commit `19392f7a08264ed00486a251f5b2098321771f94`, repository license MIT (GitHub API metadata).
   - File: https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/marketing-skill/skills/aeo/scripts/citation_tracker.py
   - Read complete source: manual local citation ledger with add/list/report/export, not autonomous collection of all models.
   - Adopted idea: stdlib local ledger/export, evidence recording. Implementation not copied.
   - Rejected: positive-only ledger as visibility-rate denominator; STRONG/EMERGING thresholds, 'citation moat' verdict, training-refresh advice for search visibility, silently resetting corrupted data; sample touching the real ledger. Our fixtures are isolated and strict errors stop execution.

## Secondary research boundaries

The two user research attachments are discovery maps, not evidence that providers are connected or proposed percentages generalize. Do not repeat exact GEO uplift/traffic/llms.txt percentages, claims of universally best vendors or '7+ runs' as a universal threshold. Use explicit dated source/design/sample if such estimates are requested separately. No llms.txt/citability/markup score is treated as measured citations. Absence of dedicated API evidence isn't proof of API nonexistence.
