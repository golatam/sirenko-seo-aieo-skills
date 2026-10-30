# Article template

Shape for an informational SEO article built from an approved brief. It is a skeleton, not a quota: drop sections the reader does not need, keep the order of the brief's outline. Title and meta are separate fields, so the body starts without an H1.

```markdown
<Lead: 2–4 sentences. Answer the main question directly, say who it applies to and its main limit.>

## <H2 from outline: reader question 1>
<Answer first, then explanation. Every number, date or price has a source link next to it:
"… по данным [Название источника](https://source.example/page) …">

## <H2: reader question 2>
<Steps, comparison table or list when the task is a process or a choice.>

## <H2: limits and alternatives>
<When this does not apply, what to do instead, what to check with a professional.>

## <H2: what to do next>
<Practical next step. The product appears here or in context, no more than product_mentions_max times in the whole text.>

<Author line only if the profile has a real author: name and link to the author page. No invented roles or credentials.>
```

## Rules

- Language and terms come from the profile `language` and `icp.vocabulary`; no translated facts from another market.
- One idea per paragraph; short sentences; tables for comparisons of three or more options.
- First-hand experience appears only as facts from the brief's `author_experience`, attributed to the author. No invented cases, clients, interviews, tests or quotes.
- Sources: primary pages actually opened; link text names the source, not "here". Every linked factual sentence is in `claims`.
- FAQ answers live in the `faq` field, not duplicated as a body section, unless the service asks for both.
- No keyword density targets, fixed word counts or filler introductions.
