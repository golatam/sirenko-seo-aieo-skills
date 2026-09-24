# Полный цикл: контрольные точки

Каждая строка применимого проекта должна попасть в stage-status. В full-cycle внешние этапы могут быть `blocked` на подтверждении; это не основание молча исключить их из отчёта.

| ID / этап | Вход | Работа и выход | Критерий перехода | Навык |
|---|---|---|---|---|
| 01 discovery | Проект, бизнес-модель, рынки | Цель, аудитория, приоритетные продукты, ограничения, KPI, brief | Домен, владелец и бизнес-конверсия определены | seo-aieo |
| 02 measurement | Аккаунты, доступы, existing tags | Реестр источников/свежести/стоимости, измерительная схема | Реальные probes; отсутствующие доступы отмечены | google-search-console-operations + ga4-project-reporting |
| 03 baseline | GSC/ranks/analytics/crawl exports | Исходные метрики, segments, dated evidence | Равные периоды, раскрыт охват и неизвестное | seo-reporting-monitoring |
| 04 market | ICP, рынок, сайты-конкуренты | Карта business/SERP/AI конкурентов, источники спроса | Не перепутаны типы конкурентов и видимость с долей рынка | seo-research-strategy |
| 05 semantics | Seeds, запросы, SERP наблюдения | Кластеры интентов, запрос→страница, gaps/cannibalization | Ручная проверка спорных кластеров, geography/date/provider | seo-research-strategy |
| 06 technical | URL inventory, raw/rendered HTML | Crawl/index/render/CWV/schema/security/trust findings | Для каждой проблемы воспроизводимый evidence и границы | technical-seo-audits |
| 07 architecture | Кластеры, inventory | URL taxonomy, hubs, link plan, navigation, facets | Каждой задаче пользователя назначена страница без искусственных дублей | seo-site-architecture |
| 08 specialized | Тип бизнеса и поисковик | Local/commerce/international/Yandex/media ветки | Применимые ветки проверены, неприменимые обоснованы | seo-specializations |
| 09 roadmap | Findings, capacity, цели | P0–P3 backlog, зависимости, owners, costs, сроки | Каждая работа проверяема и связана с фактом/гипотезой | seo-aieo |
| 10 brief | Интент, SERP, источники и экспертиза | Бриф, оригинальная ценность, доказательства, outline, CTA | Нечем подтвердить ключевое обещание → не писать его как факт | seo-content-operations |
| 11 production | Принятый бриф | Черновик, metadata, медиа, ссылки, source ledger | Редакторская/фактическая/YMYL проверка; нет выдуманной экспертизы | seo-content-operations |
| 12 ai-readiness | Контент/HTML, политики ботов | Доступность, entities, factual consistency, citation gaps | Не обещает цитирование и не требует llms.txt/AI-schema | aieo-visibility |
| 13 implementation | Проверенный scoped diff | Локальные правки, тесты, staging, rollback | Нет расширения scope и непроверенных зависимостей | technical-seo-audits + software-development-workflows |
| 14 release | Публикационный пакет/дифф | Подтверждение → выпуск → readback → change log | HTTP/DOM/каноникал/индексационные директивы и CTA проверены после выпуска | seo-content-operations |
| 15 discovery-indexing | Выпущенные canonical URLs | Sitemap/internal discovery; при согласии console submission | Readback submission; позже отдельный index-state, не гарантия | technical-seo-audits + google-search-console-operations |
| 16 authority | Активы, prospects, brand facts | Ссылочная/PR-программа, черновики, подтверждённые размещения | Согласие на outreach, реальные placement URLs, rel и referrals | seo-authority-promotion |
| 17 ai-measurement | Замороженная prompt panel | Реальные repeated answers, mentions/citations/fidelity | Ошибки и no-search отдельно; фиксированы источник/locale/version | aieo-visibility |
| 18 outcomes | Новые ranks/GSC/analytics/CRM | Клиенты/заявки, поисковая и AI-видимость раздельно | Согласованные знаменатели, цели, периоды и limits attribution | seo-reporting-monitoring |
| 19 experimentation | Гипотеза, baseline, control | Протокол теста, variation/noise, stop rules | Эффект не приписан SEO по простому совпадению дат | seo-reporting-monitoring |
| 20 maintenance | Тренды, инциденты, обновления | Refresh/prune/consolidate queue, regression checks, следующий цикл | Удаление/редиректы после согласия; сохранены ценные сигналы | seo-content-operations + technical-seo-audits |

## Режим инцидента
При резком падении сначала исключить сбой измерения, неполную историю, изменённую панель и сезонность. Затем проверить релизы, HTTP, robots/noindex/canonical, редиректы, manual actions/security через доступную консоль, crawl/index state и официальные ranking updates. Сохранить исходное состояние. Не удалять контент и не менять десятки сигналов одновременно. Авторизацию или провайдера диагностировать отдельно от состояния сайта.

## Эффект и прогноз
Сценарии трафика строить только с раскрытыми допущениями и диапазонами; использовать фактическую CTR-кривую подходящего сегмента, если она есть. Спрос, CTR и conversion rate должны иметь источники. Нет одного из входов — качественная оценка, не выдуманная финансовая модель. Серп-позиции и AI-цитаты — промежуточные показатели; конечный результат задаёт бизнес.
