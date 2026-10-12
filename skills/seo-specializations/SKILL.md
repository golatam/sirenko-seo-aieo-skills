---
name: seo-specializations
description: "Специализации SEO: локальное (Google Business Profile), интернет-магазины, международное (hreflang, рынки), картинки, видео и новости, Яндекс и Алиса. Использовать, когда просят «локальное SEO», «SEO интернет-магазина», «мультирегиональный сайт», «hreflang для рынков», «продвижение в Яндексе», «видимость в Алисе»."
version: 1.0.0
author: Sirenko SEO/AIEO Skills contributors
license: MIT
created_by: agent
metadata:
  seo:
    tags: [seo, local, gbp, ecommerce, international, media, yandex, alice]
    related_skills: [seo-aieo, technical-seo-audits, seo-site-architecture, seo-research-strategy, seo-content-operations, seo-authority-promotion, aieo-visibility, seo-reporting-monitoring]
---

# SEO Specializations

Применяй базовый SEO-процесс к фактической бизнес-модели, рынку и поверхности поиска. Модули сочетаются: например, multi-location multilingual store требует local + e-commerce + international, а не выбора одного.

## When to Use

Когда задача затрагивает GBP/local, каталог и Shopping, страны/языки, изображения/видео/News/Discover или Яндекс/Алису. Выбери все применимые модули и реальные источники.

## Входной контракт

- Домен/страницы, бизнес-модель и цель (leads/sales/readership), рынки/языки и реальные зоны обслуживания.
- Типы страниц/товаров/медиа, юридические и репутационные ограничения, owner/reviewer.
- Scope, даты, источники/экспорты, права доступа, live/staging, бюджет и baseline.
- Что разрешено: по умолчанию read-only audit + локальные DRAFT. Отсутствующие данные = `unknown`, не ноль.

## Routing: загружай только нужный модуль

| Задача | Workflow | Рабочий шаблон |
|---|---|---|
| Local / GBP / service areas / branches | [local-gbp](references/local-gbp.md) | [local-audit](templates/local-audit.md) |
| Products / variants / facets / stock / Shopping | [ecommerce](references/ecommerce.md) | [commerce-matrix](templates/commerce-matrix.csv) |
| Countries / languages / hreflang | [international](references/international.md) | [locale-matrix](templates/locale-matrix.csv) |
| Images / video / News / Discover | [media-surfaces](references/media-surfaces.md) | [media-audit](templates/media-audit.md) |
| Яндекс / Вебмастер / Алиса AI | [yandex-alice](references/yandex-alice.md) | [yandex-evidence](templates/yandex-evidence.md) |
| Основания и границы источников | [sources](references/sources.md) | — |

## Универсальный порядок

1. **Classify:** определить модель/нишу по доказательствам; не выводить реальный офис из одного schema address.
2. **Baseline:** зафиксировать измеряемый результат, source coverage, контекст страны/языка/устройства и период.
3. **Audit:** проверить representative strata и edge cases; каждому finding дать evidence, impact, confidence, owner и test.
4. **Design:** URL/content/data contract, необходимые реальные данные, политика применимости; вывести DRAFT changeset.
5. **Approve:** показать конкретные URLs/fields/old→new, риск, стоимость, rollback; ждать confirmation для внешних записей.
6. **Pilot:** только утверждённый scope; после записи перечитать точную страницу/API record, проверить rendered state и data consistency.
7. **Measure:** техническая валидность → eligibility → фактическая видимость → traffic/conversion, каждый этап доказать отдельно.
8. **Handoff:** backlog и baseline в `seo-aieo`/`seo-reporting-monitoring`; AI observations в `aieo-visibility`.

## Неподвижные правила

- Деньги, сообщения, CMS, GBP, Merchant Center, Webmaster, sitemap submission и CRM writes требуют preview + confirmation + read-back. Не менять конфиги, не устанавливать интеграции ради аудита.
- Не создавать fake offices, ложные зоны работы/отзывы, doorway city pages, фиктивный stock, invented GTIN/ratings или unsupported structured-data claims.
- Eligibility не гарантирует rich result, News/Discover inclusion, local pack или AI citation. Schema.org vocabulary и поддержка Google feature — разные проверки.
- Нет универсальных word counts, uniqueness percentages, ranking weights или обязательного review cadence. Проверяй задачу пользователя, факты и текущие официальные docs.
- UI report ≠ API capability. Сначала discovery/schema/permissions/sample read; не изобретать endpoint/MCP.
- Серп/AI ответы изменчивы. Ручная ограниченная выборка не полный рынок; масштабный сбор только через разрешённый путь с утверждённой стоимостью.
- Регулируемые ниши требуют local legal/domain review. Навык не заменяет разрешение продавать, рекламировать или давать медицинские/финансовые советы.
- Подключённые инструменты не предполагаются: нет доступа → запросить scoped export, не выдумывать результат.

## Критерий готовности

Артефакт содержит input/coverage, evidence-led findings, recommended changes, validation tests, approval state, неизвестное/ограничения и следующий owner/date.
Проверены выбранные strata и все известные критические edge cases; непроверенные части перечислены. Статусы `not applicable`, `not checked`, `blocked`, `verified` не смешиваются.
Ни технический PASS, ни закрытый checklist не обещают коммерческого эффекта.
