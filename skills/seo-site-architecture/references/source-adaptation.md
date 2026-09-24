# Architecture source decisions

Adapted concepts, not installed code; reviewed 2026-09-24.

- AgriciDaniel/claude-seo at `e77e783e38eeb738424eb72117abbd2dacdd88af`, MIT, actual `skills/seo-programmatic/SKILL.md` inspected:
  https://github.com/AgriciDaniel/claude-seo/blob/e77e783e38eeb738424eb72117abbd2dacdd88af/skills/seo-programmatic/SKILL.md
  Adopted data provenance → template value → URL uniqueness → useful internal links → quality review → progressive rollout. Rejected universal page/word/uniqueness/link-density thresholds, safe-at-scale labels and canonical preference for manual pages regardless of intent. Batch limits here are operator risk controls, not engine policy.
- Bhanunamikaze/Agentic-SEO-Skill at `69199160e18372bc5cdf9ddec20ccb9fb1b509f1`, MIT; `resources/references/quality-gates.md` and `llm-audit-rubric.md` inspected:
  https://github.com/Bhanunamikaze/Agentic-SEO-Skill/blob/69199160e18372bc5cdf9ddec20ccb9fb1b509f1/resources/references/llm-audit-rubric.md
  Adopted explicit evidence/unknowns and reviewer gate concept. Rejected minimum word counts, 30/50 location-page rules and unsupported scoring claims as universal standards.
- Google's current spam policies, doorway and scaled-content sections read 2026-09-24:
  https://developers.google.com/search/docs/essentials/spam-policies#doorways
  https://developers.google.com/search/docs/essentials/spam-policies#scaled-content
  Official policies govern substance; no magic page count or uniqueness percentage overrides them. Recheck before real rollout.

The intent/linking handoff templates and quality gates are original Hermes-native synthesis. No donor executable/installers ran, no production site was changed, no growth claims were validated. Private raw snapshots and build reports are excluded from distribution. Public pinned sources above and the repository source register (`${SEO_PACK_ROOT}/SOURCES.md`, optional checkout documentation) retain portable provenance. Broader technical provenance is in `technical-seo-audits` → `references/source-adaptation.md`.
