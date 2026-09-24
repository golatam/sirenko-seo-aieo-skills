# Identity handoff v1: research → architecture → positions → content

Это контракт передачи данных, не новая база и не доказательство корректности заполненного клиентского файла. Для каждой передачи выполнить проверки ниже, сохранить их результат. Использовать `templates/identity-crosswalk.csv`; header-only означает пустой шаблон, не готовую связь.

## Пространства идентификаторов

| Поле | Идентичность и правило |
|---|---|
| `project_id` | Пространство проекта. Одинаковый query/page/provider ID в другом проекте не совпадает. |
| `run_id` | Версия снимка/передачи и ссылки на raw inputs. Не менять query/page IDs при каждом новом замере. Ключ строки-снимка включает run_id. |
| `lane_id` | Явный ключ сегмента `(market, language, engine, device)`; словарь lane хранится в manifest. Регион провайдера сопоставляется отдельно, не выводится из языка. |
| `query_id` | Канонический ID из research queries.csv; точный query и lane неизменны. Изменение текста/рынка/языка/движка/устройства создаёт новый ID со связью на прежний, а не переписывает baseline. |
| `cluster_id` | Операционный кластер внутри lane; общая тема нескольких стран не объединяет их ключи и метрики. |
| `mapping_id` | Research query-page assignment с evidence и `mapping_status`. Architecture хранит ссылку на исходное решение, не подменяет её собственным ID. |
| `architecture_id` | Отдельный ID архитектурного решения; одна строка на входной mapping. Несколько mapping могут вести на одну страницу, но не теряют свои query IDs. |
| `target_page_id` | Устойчивый ID логической страницы в языке/регионе. Переименование proposed slug сохраняет page ID. Другой intent/язык или merge/split требует явного lineage и нового mapping/решения; не переиспользовать исчезнувший ID молча. |
| Provider keys | `provider`, `provider_account_id`, `provider_project_id`, `provider_keyword_id`, `provider_region_id` — буквальные значения из разрешённого источника. Никакой query_id не становится provider keyword ID по совпадению текста. |
| `valid_from`, `valid_to` | Интервал действия связи, ISO-8601 с timezone, начало включительно/конец исключительно; пустой конец означает открытый интервал. Историю не присоединять по сегодняшней связи задним числом. |

Минимальный join positions → crosswalk: project + provider/account/project/keyword/region + engine/device/language + интервал времени; затем `query_id` → research и `mapping_id` → архитектура. Нативные поля позиции (например `keywordId`) не переименовывать в исходном ответе: явный adapter записывает, какое поле заполнило `provider_keyword_id`. При недостатке полей или неоднозначном соответствии состояние blocked/unmapped, не fuzzy match. Несколько исходных snapshot rows после join не должны незаметно умножать один rank cell.

## Research → architecture → content

1. Проверить query foreign key и совпадение всех lane-полей. В manifest передавать project_id/run_id/lane dictionary вместе с исходными CSV; они не теряются из-за отсутствия project_id в узком research-шаблоне.
2. В архитектуре сохранить `mapping_id`, `query_id`, `target_page_id`, `mapping_status`, `target_state`, `cluster_id`, lane. Шаблон `intent-url-map.csv` навыка `seo-site-architecture` имеет эти колонки. Исходное research evidence остаётся доступным.
3. Смена предложенного URL одной и той же страницы: сохранить target_page_id/mapping_id, создать новое architecture_id/run snapshot, записать old proposed URL и new proposed URL в decision evidence. Research raw CSV не переписывать. Content получает актуальное архитектурное решение плюс исходные mapping IDs и provisional/blocked ограничения.
4. Смена самой query→page assignment: новая research mapping row и architecture decision; `supersedes_mapping_id` указывает прежнюю. Для merge/split — отдельный lineage artifact с исходными/целевыми page IDs, причинами и разрешённым migration plan. Старые метрики не переприсваивать другой странице без явной аналитической методики.
5. `provisional` остаётся provisional во всех ветках до отдельного подтверждённого исследования. Красивый slug/публикационный бриф не повышает уверенность до validated. `proposed` не превращается в existing до проверки реального URL после разрешённой публикации. Назначение owner не равно разрешению на внешний write.
6. В мониторинг передавать query_id, provider keys, lane, depth/status/observed date, expected cell roster и mapping evidence. Реальный ранжирующийся URL и желаемый target_url — разные поля; не затирать наблюдённый URL плановым.

## `rank_source` и `rankSource`

Каноническое поле внутреннего project-manifest — `rank_source`. В существующем tracker descriptor поле называется буквально `rankSource`; это **явный adapter**, а не повод редактировать descriptor.
- Если непусто только одно поле, перенести его значение в рабочее `effective_rank_source`, сохранив файл/поле происхождения.
- Если оба непусты и равны, использовать это значение; если расходятся — остановить rank branch до устранения конфликта владельцем. Молчаливого приоритета нет.
- Если оба null/отсутствуют, источник unknown; нельзя молча назначить GSC или платный Topvisor. Публичную часть исследования продолжить отдельно.
- `effective_rank_source=topvisor` требует реального Topvisor; отказ/неполнота — blocked/incomplete, не замена GSC.

## Приёмка передачи

Программно: проверить заголовки, уникальность IDs и интервалов, обязательные FK, lane consistency, количество строк до/после join, unmapped/conflicting rows и отсутствие дубликатов rank cells. Вручную: подтвердить intent/page identity, evidence и разрешение будущего изменения. Пример проверки — одинаковая фраза в ES и MX, два query IDs/Topvisor region bindings, provisional proposed pages; после переименования испанского slug каждый исходный query и rank row должен восстановиться по своему ID, provisional должен сохраниться. Синтетический пример доказывает работоспособность контракта, не клиентских данных.
