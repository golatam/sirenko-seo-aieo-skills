# Observation contract v2 and denominator rules

Schema v2 separates requested/prompt `locale` from observed `response_locale`. V1 is deliberately rejected rather than silently reinterpreted: preserve the old ledger, recover requested locale from the frozen panel manifest, recover actual response locale from capture/review (or null if unknown), then write a separately versioned converted ledger with provenance. Never copy a desired locale into an observed-language field as a guess.

This contract is deliberately stricter than arbitrary vendor exports. Convert exports only after reading their semantics. No network calls or provider collection occur in the summarizer. It validates structure and accounting, not truth or completeness. JSONL: one UTF-8 JSON object per line; blank lines, duplicate JSON keys, NaN, missing/extra fields or invalid values fail the entire run (exit 2; no summary). Empty input returns an explicitly empty report. No silent 'skip bad rows' mode.

## Required fields (all must be present)

| Fields | Type and meaning |
|---|---|
| `schema_version` | integer `2`, not boolean |
| `observation_id` | globally unique stable ID for one captured attempt |
| `run_id`, `repeat_id` | nonempty strings identifying collection wave and attempt; retries/new dates use new run/repeat |
| `panel_id`, `panel_version` | frozen roster identifier and version |
| `prompt_id`, `prompt_version`, `prompt_text` | exact prompt and version; translated/paraphrased prompts have distinct IDs, with family mapping in manifest |
| `engine`, `model`, `surface` | observed labels; use literal `unknown` if model not displayed, never infer a model from product name |
| `source_type` | `ui`, `api`, `aggregator`, `simulated`; simulated requires `synthetic=true` |
| `search_mode` | requested `auto`, `forced`, `off`, `unknown` |
| `search_used` | actual `true`, `false`, `null` unknown; source list alone does not establish search execution; off+true is contradictory |
| `locale`, `market`, `intent` | nonempty frozen roster-defined strings; locale is requested/prompt language/locale, market is geography; do not infer country from language |
| `response_locale` | observed response language tag, `mul` for mixed, `und` for reviewed but undetermined, or null if not observed/unknown; must be null for error/unknown status. Tag shape is checked, not registry membership or language correctness. Not part of frozen identity; never auto-detect or copy from requested locale without evidence |
| `brand_scope` | `branded` or `unbranded`, referring to prompt not answer |
| `observed_at` | RFC3339 timestamp with timezone, e.g. `2026-09-24T12:00:00+02:00`; offset hour/minute ranges are checked before datetime parsing (no normalization of malformed offsets such as `+00:99`); grouping date uses UTC |
| `status`, `error` | `ok` with null error; `error`/`unknown` with nonempty reason |
| `raw_answer` | captured text for ok; null otherwise, not recreated text |
| `evidence_ref` | nonempty artifact locator for original capture/error; script does not open it |
| `mention`, `recommendation` | independently adjudicated boolean or null unknown |
| `mention_quote`, `recommendation_quote` | exact raw-answer substring when respective judgment true; null otherwise |
| `citations` | list of citation-claim objects; `[]` means checked and no citations; null means unavailable/not reliably parsed |
| `exclusion_reason` | null or nonempty predefined exclusion reason; retain excluded attempts |
| `synthetic` | strict boolean; fixtures require CLI `--allow-synthetic`; grouping isolates them even in mixed input |

`error`/`unknown` status must have raw answer, response locale, mention, recommendation, both judgment quotes, and citations all null. A partial/truncated or uncertain response is not a successful negative. A complete refusal can be coded ok if collection succeeded and the preregistered eligibility rule allows it; log a predefined exclusion if not, never a post-hoc exclusion based on brand absence.

`mention=true` requires a quote containing a CLI-approved literal alias at Unicode-aware token boundaries (case-insensitive), verified in at least one exact quote occurrence in the original answer. Cutting `Example Brand` out of `NotExample Brandish` cannot create valid boundaries. This is a mechanical check, not semantic identity recognition: review ambiguous names, legal/trading names, transliterations and homonyms manually against the versioned alias registry. `recommendation=true` also requires an adjudicated mention and a direct endorsement quote. False judgments can reject ambiguous homonyms; document that decision in capture evidence.

## Citation-claim objects

Exactly `{url, claim_quote, source_quote, fidelity, evidence_ref}`. URL must be absolute http(s), with valid hostname, no credentials, backslashes or whitespace. `claim_quote` must be an exact answer substring. `fidelity` is one of `supported`, `partial`, `unsupported`, `unverifiable`, `not_reviewed`. All need a nonempty evidence reference. Reviewed statuses (first three) require a nonempty source quote; other two may have null source quote. Follow the manual protocol before assigning reviewed status. A claim paraphrase invented by an analyst is not an exact claim quote.

An object is one citation–claim pair, not one citation marker or one URL. A URL supporting two distinct claims is two units. Repeated identical objects within an answer dedupe and are counted in `duplicate_citations_removed`; same literal URL+claim with conflicting judgments fails. Do not canonicalize away redirect/tracking variants automatically: resolve and document in the capture layer while retaining original URLs. Only owned-domain pairs enter fidelity statistics; third-party sources stay in raw evidence for separate analysis.

## Domain rules and exact dedupe

Pass each approved owned hostname as `--domain`. Hosts must be ASCII (including a verified IDN A-label such as `xn--fa-hia.example`); the stdlib tool deliberately rejects Unicode U-labels rather than applying lossy IDNA2003 (`faß.example` must not become `fass.example`). At ingestion, obtain a verified A-label using an approved modern non-transitional IDNA method and preserve the original displayed URL plus conversion evidence. Lowercase and at most one terminal DNS root dot are normalized for matching; repeated trailing dots fail. Original URL/IDs are retained. Subdomains are excluded unless `--include-subdomains`. Domain aliases/ccTLDs must be explicit; there is no public-suffix or ownership inference. Boundary matching is `host == approved` or explicitly allowed `host.endswith('.'+approved)` — not substring matching.

Repeated `observation_id` with identical JSON values (key order/formatting ignored) is an exact duplicate. Any changed field under that ID fails. Different IDs occupying the same cell (panel/version, engine/model/surface/source/mode, locale/market/intent/brand scope/synthetic, run, prompt/version, repeat) fail rather than silently discarding a legitimate repeat. Same prompt identity with different text/locale/market/intent/brand scope within a panel version fails. Distinct repeats with identical answers remain separate observations.

## Rates and evidence scope

Groups retain panel/version, engine/model/surface/source type, requested search mode, requested locale/market/intent, branded/unbranded, synthetic flag, UTC date and actual search state (`search`, `no_search`, `unknown`). `eligible_response_locales` reports observed-language counts among eligible answers (`unknown` key for null); language drift is retained, not a reason to change prompt ID or drop an answer. Outcome rates remain requested-panel rates; for actual-language-specific rates do a separately labelled stratified analysis. A changed response language cannot create a new measurement cell. No global visibility rate is produced. Valid no-search answers remain in their own group; no-search and unknown-search are not 'errors' or silently dropped.

Eligible answers = unique `status=ok` observations with no exclusion reason. Counts of errors, unknown status and exclusions are explicit; these counts can overlap (an errored observation can also carry an exclusion). Metric unknown counts apply only to eligible answers.

- **Mention/recommendation**: true labels / known true-or-false labels among eligible answers. Nulls reported as `unknown`; never treated as false.
- **Owned citation answer rate**: eligible answers with at least one matching owned-domain citation / eligible answers with known citations list, including empty lists. Null lists are unknown. Counts answers, not citation objects.
- **Fidelity**: supported owned citation–claim pairs / reviewed owned pairs (`supported+partial+unsupported`). Unknown = unverifiable+not_reviewed. Partial is not fully supported.
- **Fidelity review coverage**: reviewed owned pairs / all observed owned pairs; label counts included. High fidelity with low review coverage is not a clean bill of health.
- All rate objects expose `numerator`, `denominator`, `unknown`, `rate` as fraction or null for zero denominator, never a fabricated 0%.

This is descriptive attempt-weighted accounting, not a population estimate: prompts with more repeats receive more weight. Reconcile to the frozen manifest and balance/match repetitions before comparisons. A script cannot know an attempt was never collected. For equal-prompt metrics or confidence intervals, design a separate reviewed analysis with prompt/date clusters; repeated answers are correlated. Do not use naive independent-binomial intervals or call a pre/post movement causal.

## Panel manifest (outside JSONL)

Preserve: project, approved domain/alias registry + versions, source provenance, roster rows `{prompt_id,prompt_version,text,family,locale,market,intent,brand_scope}`, planned engines/model/surfaces/search modes, expected runs/repeats/date windows, missing attempt inventory, collection/account context (signed-in/out and personalization settings without secrets), exclusions established before collection, parser/coder version, artifact directory/access policy and budget. Model/surface changes create distinct strata; unexplained drift blocks a like-for-like comparison.
