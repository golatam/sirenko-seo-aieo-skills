# Зависимости: bundled и host — разные вещи

## Внутри пакета

Ровно 13 каталогов в `skills/` (12 основных и вспомогательный `claim-verification`); роли и владельцы — в [README](../README.md). Три локальные утилиты:

| CLI | Зависимости | Что не делает |
|---|---|---|
| `html_evidence.py` | Python stdlib | Не делает HTTP/DNS, JS/rendering, crawl/index/rank/CWV |
| `summarize_observations.py` | Python stdlib | Не собирает AI-ответы, не вызывает провайдеров, не проверяет истинность evidence |
| `validate_pack.py` | Python + PyYAML | Не исполняет найденный skill code, не проверяет авторизацию, не устанавливает зависимости |

Runner и упаковочный checker требуют тот же PyYAML; отдельный pytest/Node/npm не нужен. Проверенная локально версия Python — 3.13.5, PyYAML — 6.0.2; зафиксированная зависимость в [requirements.txt](../requirements.txt). Hosted CI должен использовать отдельное настроенное Python-окружение, не production/системный Python оператора.

## Необязательные внешние навыки

Имена ниже — необязательные навыки, которые могут быть установлены отдельно; они **не входят в пакет**. Устанавливать их автоматически запрещено. Сначала проверка, что навык есть в среде, и чтение его инструкции. `related_skills` — метаданные маршрутизации, не импорт и не гарантия наличия инструмента.

| Точное имя | Когда нужно | Безопасный fallback при отсутствии |
|---|---|---|
| `competitor-analysis` | Детальный анализ конкурентов в research/content | Выполнить ограниченный evidence-first research по included методике, явно ограничить охват |
| `humanizer-ru` | Дополнительная редактура текста | Ручная редактура по included workflow; не добавлять вымышленные факты/экспертизу |

Машиночитаемая декларация: [host-dependencies.json](host-dependencies.json). Валидатор принимает **только явно перечисленные** внешние имена (или реально найденные внутри переданного skill root); неизвестные и ошибочные имена не игнорирует. Навыки пакета (включая вспомогательный) нельзя объявить внешними, дубликаты и malformed declarations отклоняются. Результат `external_availability_verified: false` намеренный: проверка декларации не устанавливает доступность навыков.

Доступ к Google, MCP, CRM и рассылкам пакет не поставляет: используйте уже одобренные в вашей среде коннекторы и helper-ы, а при их отсутствии оставляйте источник blocked.

## Внешние источники и runtime

- **GSC**: разрешённый read-only MCP/API/export. Discovery → точная схема → `list_sites` → точное property → минимальный запрос → totals/coverage. Отсутствие error не доказывает полную выгрузку. OAuth token scopes/refresh не расширять автоматически.
- **GA4**: host Google integration и нужное property. Sheets/Drive создаются только по отдельному запросу/approval; локальному отчёту write scopes не нужны.
- **Topvisor**: существующий одобренный tracker/API и `${SEO_TRACKER_DIR}`, только если реально совместимы. Node scripts из [host tracker reference](../skills/seo-reporting-monitoring/references/topvisor-central-tracker-cron.md) — примеры другой реализации, в этом пакете этих `.mjs` файлов **нет**. Не копировать/инсталлировать внешний сервис автоматически. Read price → явное согласие на стоимость → один job → полная матрица → отчёт. `dry-run` не доказывает отсутствие write.
- **Bing/Яндекс/GBP/Merchant/AI providers**: свои аккаунты, права, схемы и бюджеты; UI не означает API. Доступность каждого источника проверяется отдельно. Готовых коллекторов и ключей нет.
- **Crawler/CMS/outreach/market data**: approved host tools или разрешённые экспорты. Полный crawler, CMS deployment, paid keyword/backlink data, AI collection, cron и notifier не являются зависимостями offline-тестов.

При отсутствии интеграции выполняется только доказуемая часть: blocked/unknown остаётся в manifest. GSC не заменяет Topvisor, readiness не заменяет AI visibility. Пакет не меняет конфигурацию среды, токены, сервисы или расписания.
