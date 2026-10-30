# Article QA checklist

Run before handing an article over: in service mode as the self-check before writing `article.json`, and by any reviewer producing `kind: "llm"` checks in a QA file (`schemas/qa.schema.json`). Fact checking against sources belongs to `claim-verification` (`kind: "claim"`). Each item is pass/fail with a short reason; a failure becomes a fix with `where`, `problem`, `suggestion`. Full review gates are in [editorial workflow](editorial-workflow.md).

| # | Check (name) | Passes when |
|---|---|---|
| 1 | structure | Body has no H1; H2 follow the brief outline; lead answers the main question; limits/alternatives present where relevant. |
| 2 | title_length | `title` is 1–60 characters and matches the page's actual promise. |
| 3 | meta_length | `meta` is 1–155 characters, no keyword stuffing, no promise the page does not keep. |
| 4 | claims_sourced | Every number, date, price, percentage and checkable fact in `body_md` is in `claims` with an existing `source_id`; `claims[].text` occurs in the body. |
| 5 | sources_linked | Each source used in the body is an ordinary Markdown link next to the supported sentence and listed in `sources`. |
| 6 | no_fabrication | No invented authors, credentials, cases, clients, interviews, tests, quotes or statistics; author experience only from the brief/profile. |
| 7 | product_mentions | Product mentioned no more than `product_mentions_max` (from the brief / profile `product.mentions_max`); `product.constraints` and `brand_negatives` respected. |
| 8 | faq | 3–6 questions from the brief, each answered briefly; factual answers follow check 4. |
| 9 | internal_links | Links only to existing site URLs from the brief, with descriptive anchors. |
| 10 | language | Profile language and reader vocabulary; no machine-translated phrasing or AI clichés (use `humanizer-ru` interactively). |
| 11 | ymyl | Health, legal, tax or financial advice is general, states its limits and suggests a qualified professional; flags the need for expert review. |

Overall `passed` is true only when every check passes. Word count, AI-detector scores and SEO-tool scores are not checks.
