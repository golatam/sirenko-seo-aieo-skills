---
name: seo-authority-promotion
description: "Use when planning SEO offsite promotion and earned media."
version: 1.0.0
author: Hermes Agent
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [seo, offsite, backlinks, digital-pr, outreach]
    related_skills: [seo-aieo, seo-research-strategy, seo-content-operations, seo-specializations, seo-reporting-monitoring, business-messaging-integrations]
---

# SEO Authority & Promotion

Продвигай полезные активы к релевантной аудитории, а не покупай сигналы ранжирования. Результат — проверяемые earned placements и бизнес-эффект; число ссылок само по себе не цель.

## When to Use

Для backlink/mention inventory, link gap, digital PR, editorial assets, адресного outreach и проверки earned placements. Не заменяет технический аудит и не разрешает отправку.

## Вход и режим

Зафиксируй домен/бренд и алиасы, рынки/языки, аудиторию, предложение, запрещённые темы, владельца, бюджет, срок, baseline и доступные экспорты. Режим: `inventory`, `prospect`, `asset`, `draft`, `approved-send`, `verify`, `measure`.
По умолчанию — read-only исследование и локальные DRAFT, без платных вызовов, отправки, публикации и изменений CRM. Недостаток данных = `unknown`, не правдоподобная метрика.

## Обязательный цикл

1. **Inventory:** ссылки и упоминания, происхождение, даты, покрытие, дубли; проверка реальных страниц.
2. **Prospects & fit:** тематическая/географическая релевантность, редакционная деятельность, аудитория и причина контакта.
3. **Editorial asset:** оригинальное исследование, инструмент, экспертный материал или данные; проверка метода, прав, цифр и disclosure.
4. **DRAFT outreach:** персонализированный текст на языке адресата; ссылка — редакционный выбор, не условие сделки.
5. **Approval:** точный sender, адресат, subject/text, актив/версия, бюджет и действие; подтверждение именно пакета.
6. **Send & read-back:** действующий канал и его approval-policy; перечитать точное сообщение в треде/Sent, сверить ID и текст.
7. **Placement verification:** опубликованная страница, href/final URL, HTTP, rel, контекст, disclosure; недоступность не равна удалению.
8. **Measurement:** сопоставимые периоды, referrals/leads, earned mentions и аудитория; SEO/AIEO-корреляция не причинность.

Промежуточный режим завершается своим артефактом и следующим gate, не заявлением о завершении всего цикла.

## References — загружай по необходимости

- [references/inventory-prospects.md](references/inventory-prospects.md): источники, dedupe, gap, проверка, квалификация.
- [references/earned-promotion.md](references/earned-promotion.md): активы, PR, сообщения, approval, placements, измерение, stop rules.
- [references/sources.md](references/sources.md): официальные основания, донор, adopt/reject.
- [templates/campaign.md](templates/campaign.md): паспорт, gates, DRAFT, approval, итог.
- [templates/inventory.csv](templates/inventory.csv), [templates/prospects.csv](templates/prospects.csv), [templates/placements.csv](templates/placements.csv): evidence-ledgers.

## Жёсткие ограничения

- Публичный поиск не исчерпывающий backlink index. «Не найдено» ограничено методом/выборкой.
- DR, DA, vendor spam score, Common Crawl centrality — разные величины, не Google scores; не усредняй их в «authority».
- Нет универсальных норм anchor ratio, количества ссылок, follow ratio, TLD-quality или месячного прироста.
- Запрещены покупка ranking links, PBN, обмены ради рейтинга, скрытый advertorial, fake reviews, астротурфинг, массовые unsolicited сообщения и Wikipedia self-promotion.
- Спонсорство — отдельный рекламный канал с disclosure и квалифицированными ссылками, не earned SEO.
- Не делай автоматический disavow и не советуй по одному spam score. Только evidence packet и экспертное решение, отдельное подтверждение вне этого workflow.
- DRAFT/prospect list не разрешают рассылку, CRM-запись, расход денег или публикацию. Внешнее изменение: preview → confirmation → exact execution → read-back.
- Для CRM/сообщений загрузить `business-messaging-integrations` и email/LinkedIn skill. Standing approval rules сохраняются; retired endpoints не переносить.
- Ответ адресата не разрешает от имени пользователя согласовать цену, раскрытие информации, созвон или условия.

## Проверка результата

Выдай scope/coverage → observations → qualified prospects → asset/drafts → approved/unapproved actions → verified placements → results/limitations.
Для finding обязательны source URL/export, checked_at, статус, факт отдельно от гипотезы, next action/owner. Counts и dedupe считать кодом.
`sent`, `live`, `indexed`, `referral`, `converted` — разные статусы с отдельными доказательствами.
Не обещай размещение, позиции или цитирование ИИ. В `seo-reporting-monitoring`/`aieo-visibility` передай реальные исходники, не синтетический балл.
