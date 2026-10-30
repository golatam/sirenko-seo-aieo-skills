# Service mode: brief and article files

Used when a service runs this skill unattended (see the Service mode section of SKILL.md). `step` in `service.json` selects the work: `brief` or `article`. Contracts are `schemas/brief.schema.json` and `schemas/article.schema.json` at the plugin root; if the plugin is installed without them, the field lists below are the contract.

Common inputs: `profile` (site profile YAML: `language`, `icp`, `product.mentions_max`, `product.constraints`, `brand_negatives`, `author`). Read-only public fetches of sources are allowed; paid calls and any external write are not.

## step: brief

Input: `inputs.topic` — one item of a topics file (title, slug_hint, keywords, intent, hub, role, evidence); optionally the site's URL list for internal links.

1. Define the reader and the task from `icp` and the topic intent; write `audience` and `search_intent` as one or two plain sentences each.
2. Build `outline` as an argument plan, following [editorial workflow](editorial-workflow.md): each H2 answers one reader question; `points` say what the section establishes; `sources` are primary URLs you actually opened. A section without a source is fine for explanations, not for numbers.
3. `author_experience`: copy only facts from `profile.author.experience` relevant to this topic. Empty list if none fit; never add new ones.
4. `product_mentions_max`: `profile.product.mentions_max` (0 if absent).
5. `faq`: 3–6 real follow-up questions from queries, People Also Ask or the outline; questions only.
6. `internal_links`: existing site URLs only (from inputs or a verified fetch); the hub pillar first for a support page. No links to planned pages.
7. `title` ≤ 60 and `meta` ≤ 155 characters, in the profile language, with the actual promise of the page.

Fields: `topic_title`, `slug` (a-z0-9-), `title`, `meta`, `audience`, `search_intent`, `outline[] {h2, points[], sources[]}`, `author_experience[]`, `product_mentions_max`, `faq[] {q}`, `internal_links[] {url, anchor}`, optional `reasons[]`.

Not enough sources for the topic: write the brief narrowed to what is supported and list the gaps in `reasons`.

## step: article

Input: `inputs.brief` — a brief file from the previous step.

1. Write `body_md` by [article template](article-template.md): no H1 (the title is separate), H2 from the outline, answer first, sources as ordinary Markdown links next to the supported sentence.
2. Every number, date, price, percentage and checkable fact in `body_md` goes into `claims[] {text, source_id}` with `text` copied exactly from the body, and `source_id` pointing to `sources[] {id, url, title}`. Use only sources you opened and that support the exact wording.
3. No source for a number: remove the number or rephrase without it, and note it in `reasons`. Never invent statistics, cases, quotes, clients or author experience.
4. Mention the product at most `product_mentions_max` times; respect `product.constraints` and `brand_negatives`.
5. `faq[] {q, a}`: answer the brief's questions briefly; factual answers follow rule 2.
6. `word_count`: count words of `body_md` with a tool, not by estimate.
7. Run the [QA checklist](qa-checklist.md) on the result and fix what fails before writing the file.

Fields: `slug`, `title` (≤60), `meta` (≤155), `body_md`, `faq[]`, `sources[]`, `claims[]`, `word_count`, optional `reasons[]`.

Before finishing, parse the written file as JSON and check required fields, lengths and that every `claims[].source_id` exists in `sources[].id`.
