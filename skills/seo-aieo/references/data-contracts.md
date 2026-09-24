# Контракты артефактов

## Общий provenance
На каждый набор: project_id, source/provider, exact property/domain, collection_method, collected_at (ISO-8601 с timezone), data_period, source_timezone, market, language, device/surface, filters, pagination/coverage, raw/evidence path, known limits. Не перезаписывать исходные ответы; derived-таблицы хранить отдельно. Для крупных файлов считать SHA-256 инструментом. Не хранить ключи, cookies, токены или личные данные посетителей.

`unknown`/`null` обозначает недоступное; 0 — измеренный ноль. `status=error` не преобразуется в нулевую видимость. Валюты и units явные. CSV UTF-8 с корректным quoting; при переносе в Sheets/Excel защищать текстовые cells от formula injection (`=`, `+`, `-`, `@`), сохраняя raw вне таблицы.

## Evidence ledger
`templates/evidence.csv`: один атомарный факт на строку, ID стабилен в этом запуске. `classification=observed|derived|hypothesis|unknown`. Для derived указывать формулу и input IDs. `scope=URL|template|site|panel|account`, sample_size и limitations не дают распространять факт одной страницы на весь сайт.
HTTP/DOM fragment, console response, screenshot или экспорт подтверждают наблюдение. Рекомендация отдельно от наблюдения и предполагаемой причины. Ложное срабатывание сохранять с объяснением, не прятать.

## Ключевые таблицы
- Семантика: устойчивый research `query_id`, exact query, market/language/engine/device, intent, cluster_id; назначения `mapping_id`, `target_page_id`, `target_url`, `target_state=existing|proposed|none`, `mapping_status=validated|provisional|blocked`. Provider `keyword_id` — отдельный внешний ID, не замена query_id. Использовать шаблоны `seo-research-strategy` и явный crosswalk из `references/identity-handoff.md`.
- URL inventory: requested/final URL, status/redirects, canonical(s), robots directives, raw/rendered, template, title/H1, discovery_source, fetched_at, evidence. `indexable_by_observed_signals` не равно `indexed`.
- Positions: keyword ID, engine, region, language, device, date, position/null, explicit data_status (`ranked|out_of_range|missing|error|pending`), actual URL, provider depth/expected cell count. Тексты ключей без ID недостаточны для дедупликации разных рынков.
- AI observations: строгий формат `aieo-visibility`; хранить raw answer отдельно от ручной интерпретации, versions панелей и провайдера не смешивать.
- Outcomes: period, cohort/landing_url, channel/source, key-event definition, numerator/denominator, currency, attribution_method, completeness. GA4 и GSC имеют разные методы и часовые зоны, 1:1 совпадения не требовать.

## Сквозные идентификаторы
Обязательные правила query/page/provider identity, смены URL, provisional-статуса и соответствия `rank_source` ↔ descriptor `rankSource`: `references/identity-handoff.md`. Шаблон связи: `templates/identity-crosswalk.csv`. Перед передачей в content/rank/reporting проверить foreign keys и lane, а не соединять по тексту запроса или текущему slug.

## Stage и change log
`templates/stage-status.csv`: одна строка на каждый ID из lifecycle. Статусы `not_started|in_progress|blocked|not_applicable|verified`. Для verified обязательны artifact и verification_evidence. Для not_applicable — reason; для blocked — blocker и следующий безопасный шаг.
`templates/backlog.csv`: не менять статус в done только по успешному API-ответу. Проверять exact target readback. Согласование в файле — журнал, а не самостоятельная авторизация; действуют реальные подтверждения пользователя и policy инструмента.

## Расположение
`${PROJECT_DOCS_DIR}` хранит brief, решения и ссылки. Подробные выгрузки и проверки — `${SEO_ARTIFACTS_DIR}/<project>/seo/<run-id>/`. Не использовать папку skills как базу клиентских данных. У навыков только общие методики, обезличенные примеры и тестовые fixtures с явной меткой synthetic.
