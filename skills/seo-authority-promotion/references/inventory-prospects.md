# Inventory → verified map → qualified prospects

## Контракт

**Input:** domains/URLs, прежние домены и бренды, алиасы, рынки, конкуренты по intent, даты, разрешённые экспорты и история кампаний.
**Output:** `inventory.csv`, coverage note, gap candidates, `prospects.csv`, review queue/exclusions.
**Validation:** источник и дата каждой строки; проверенные ссылки отделены от индексных наблюдений; prospect прошёл hard gates; нет утверждения о полном интернете.

## 1. Источники и baseline

1. Опиши источники: пользовательский Links/mentions export, подключённый read-only провайдер, публичный поиск и проверка известных страниц. Discovery инструмента не доказывает доступ к аккаунту/оплаченному тарифу.
2. Для экспорта: provider/snapshot/time, domain vs URL scope, live/historical, фильтры, pagination, заявленное и выгруженное число строк. Несовпадение totals — blocker для «полный».
3. Метрики хранить `(provider, metric_name, value, scale, observed_at, scope)`. DA/DR и centrality не смешивать. Новый провайдер = отдельный временной ряд.
4. Публичный поиск: точный бренд/алиас + тема/страна, исключение собственного домена, найденные редакционные/партнёрские материалы. Сохраняй query/locale/date и URLs. Snippet — discovery, не доказательство ссылки.
5. Common Crawl/domain graphs не подтверждают текущие backlinks/анкоры; search result count не total mentions. Нет базы → «public discovery», не полный backlink audit.

## 2. Нормализация и dedupe

- Сохраняй raw URLs/IDs неизменными; normalized key отдельно. Не удаляй параметры языка/варианта/содержимого произвольно.
- Link-level key: source page + resolved target + context/position. Page-level и domain-level aggregates отдельно. Sitewide links — не независимые endorsements.
- Domain parsing требует публичных суффиксов; если проверенного parser нет, считай hostname, не ошибочно последние два label. Не устанавливать dependency автоматически.
- Пометь syndication, зеркало издателя, redirect, sitewide/footer. Несколько copies одного пресс-релиза не independent PR.
- Entity match: бренд + продукт/официальная ссылка/география; одно имя недостаточно. Типы: linked, unlinked, ambiguous, syndicated, not checked.

## 3. Проверка страниц

Укажи sample strategy: приоритетные placements + случайная выборка остального, а не только успешные строки.
1. Открой точный source URL; сохрани checked_at, HTTP, redirect chain и evidence locator. Rate limits/robots/ToS соблюдать, доступ не обходить.
2. Проверь actual anchor в HTML/rendered DOM: href, resolved target, текст, rel tokens (`nofollow`, `sponsored`, `ugc`, отсутствует), контекст и section. Отсутствие rel не доказывает передачу ranking credit.
3. Проверь target HTTP/final URL/canonical и соответствие цитируемому материалу. 404 с backlinks → ticket в `technical-seo-audits`; не redirect всего на homepage.
4. Meta robots/X-Robots-Tag отмечать при доступности. 200/no-noindex не доказывают индексирование; чужой URL без подтверждения = `index status unknown`.
5. JS/login/429/timeout = `unverifiable`, не `removed`. Потерю подтверждай доступным повторным чтением нужного контекста.
6. Для new/lost нужны сопоставимые snapshots. Vendor first_seen ≠ publication date; исчезновение из экспорта ≠ удаление с сайта.

## 4. Gap и fit

Выбирай конкурентов по ICP/предложению/рынку. Сравни одним provider, scope, датой и фильтрами. Gap без базы — только discovery hypothesis.
Для каждого competitor link прочитай страницу: почему он там (данные, инструмент, реестр, обзор, реклама)? Не копируй спам. Наличие чужой ссылки не означает возможность получить свою.

| Hard gate | Доказательство | При провале |
|---|---|---|
| Audience fit | Конкретная reader problem, тема, язык/география | Exclude независимо от DA |
| Editorial legitimacy | Реальные авторы/редакция, оригинальные материалы, прозрачность | Link farm/PBN/скрытая продажа ranking links → exclude |
| Honest contribution | Что добавляет актив именно этой странице/рубрике | «Нам нужна ссылка» → revise asset |
| Contact route | Публичный профессиональный адрес/форма или существующий тред, source URL | Не угадывать личный email и не покупать список |
| Rights/sensitivity | Право раскрывать данные, клиентские имена, результаты | Hold |
| Contact policy | Suppression, отказ, дубли, другой активный outreach, правила рынка/канала | Stop или legal review |

После gates ранжируй high/medium/low по релевантности, новизне, reachability, effort. Это эвристика, не вероятность размещения; балл не компенсирует hard fail.

## 5. Reclamation и риск

Unlinked mention → предложить полезную читателю ссылку без требования dofollow. Broken citation → восстановленный оригинал/эквивалент, не покупка expired domain. Wrong claim → factual correction с источником, не оплата удаления правдивой критики.
Suspicious backlinks → evidence/history review; не объявлять penalty/negative SEO по TLD, языку, скачку счётчика.
Disavow — advanced risky tool: значительное число искусственных/спамных ссылок **и** manual action/вероятность action. Большинству сайтов он не нужен. Только экспертный evidence packet, без автоматической генерации и загрузки disavow.[16]

## Evidence basis

Адаптированы source/verification gates донора [1], отвергнуты его численные нормы и blended score. Ограничения link manipulation — [5]. Полные URL/provenance: [sources.md](sources.md).
