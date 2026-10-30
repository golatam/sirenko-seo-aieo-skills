# Схемы режима service

JSON Schema (draft 2020-12) для файлов, которые навыки пишут, когда их запускает сервис через Claude Agent SDK без человека в чате. Сервис проверяет файл по схеме и только потом сохраняет результат. В обычном чате схемы не нужны.

| Файл | Кто пишет | Шаг |
|---|---|---|
| `topics.schema.json` | `seo-research-strategy` | темы для сайта |
| `brief.schema.json` | `seo-content-operations` | `step: "brief"` |
| `article.schema.json` | `seo-content-operations` | `step: "article"` |
| `qa.schema.json` | `claim-verification` (`kind: "claim"`); проверки по чеклисту статьи — `kind: "llm"` | проверка статьи |

## Как запускать

Сервис кладёт в рабочую папку `service.json` (или передаёт те же поля в промпте). Пути — относительно этой папки:

```json
{
  "mode": "service",
  "skill": "seo-content-operations",
  "step": "brief",
  "profile": "site-profile.yaml",
  "inputs": { "topic": "in/topic.json" },
  "output": "out/brief.json"
}
```

- `mode` — всегда `"service"`; без него навык работает как обычно, в диалоге.
- `profile` — профиль сайта по образцу [templates/site-profile.yaml](../templates/site-profile.yaml).
- `inputs` — входные файлы шага: для тем — выгрузки (`gsc`, `yandex`, `sitemap`, `serp`); для брифа — `topic` (один элемент `topics[]`); для статьи — `brief`; для проверки — `article`.
- `output` — ровно один JSON-файл, который навык создаёт.

Навык в этом режиме не задаёт вопросов, ничего не публикует и не пишет во внешние системы. Не хватает данных — пишет файл с пустым или суженным результатом и причиной в `reasons`.

## Как проверять

Python:

```python
import json
from jsonschema import Draft202012Validator
schema = json.load(open('schemas/article.schema.json', encoding='utf-8'))
Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER).validate(data)
```

Node: `Ajv2020` из `ajv/dist/2020` вместе с `ajv-formats`.

Схема не проверяет связи между полями — это делает код сервиса:

- каждый `claims[].source_id` есть среди `sources[].id`, а `claims[].text` встречается в `body_md`;
- в `body_md` нет цифр вне `claims` (грубая проверка: числа в тексте против чисел в `claims`);
- упоминаний продукта не больше `product_mentions_max` из брифа;
- `qa.passed` равно «все `checks[].passed` истинны».
