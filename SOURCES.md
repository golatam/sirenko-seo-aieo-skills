# Источники, происхождение и лицензирование

Пакет — независимый Hermes-native синтез методик, оригинальные шаблоны и локальные Python-утилиты. Материалы исходной ревизии датированы **2026-09-24**; эта переносимая упаковка сохраняет публичные pinned references, но не перевыполняет историческую web-проверку и не доказывает актуальность продуктовых API/политик навсегда.

## Границы лицензии

[MIT](LICENSE) применяется к оригинальным материалам этого пакета. Публичные страницы/репозитории, на которые даны ссылки, сохраняют свои лицензии; наша MIT-лицензия не перелицензирует их. Donors использовались выборочно как reference material, не устанавливались и не поставляются как исполняемые плагины. Не импортированы их installers, hooks, commands, dependencies или целые skills. Прямое копирование при будущих обновлениях требует отдельной проверки лицензий/notices.

Сохранён существовавший полный [MIT notice AgriciDaniel](skills/seo-authority-promotion/references/sources.md#donor-license-notice). Другие donor-файлы не включены целиком: публичные pinned source/LICENSE links и границы adopt/adapt/reject лежат в соответствующих source references. Имена публичных авторов и commit IDs — атрибуция, не клиентские идентификаторы.

## Выборочно изученные доноры

| Донор | Проверенный в исходной ревизии commit | Суть заимствованной идеи / локальное решение |
|---|---|---|
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | `e77e783e38eeb738424eb72117abbd2dacdd88af` | Категории technical/programmatic/backlinks, evidence и staged rollout; без magic scores/quotas/disavow automation |
| [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) | `69199160e18372bc5cdf9ddec20ccb9fb1b509f1` | Evidence/impact/fix, unknowns и quality gates; без вымышленных порогов/гарантий |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | `e818d5e38551a931333381d69c43da6e767ec775` | Research/draft/rewrite/CRO separation; без обязательной плотности/word count/plugin commands |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | Customer evidence и intent-driven planning; без фиксированных scoring weights |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | `3777930184a10b25ab36bb2fc4da6c0f6cfcc187` | Artifact contracts и no invented volume; без KD-based guarantees |
| [promptwatch-com/skills](https://github.com/promptwatch-com/skills) | `36fb1231174bef63980f260500a9dbd1dd0ff18d` | Owned/third-party citations и bounded comparisons; без вымышленных Hermes tools |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | `19392f7a08264ed00486a251f5b2098321771f94` | Локальный evidence ledger; наш summarizer написан независимо, не перенос donor tracker |

В исходных reference-файлах root licenses первых пяти отмечены как прочитанные MIT; для последних двух MIT был определён через GitHub metadata. Это разные уровни проверки, не одинаково полный license audit. Donor runtime/эффективность не подтверждались. Публичные ссылки сохранены, частные donor snapshots/build reviewlogs сюда не экспортированы.

## Подробная карта решений

- [Research](skills/seo-research-strategy/references/sources.md)
- [Technical](skills/technical-seo-audits/references/source-adaptation.md)
- [Architecture](skills/seo-site-architecture/references/source-adaptation.md)
- [Content](skills/seo-content-operations/references/sources.md)
- [AI visibility](skills/aieo-visibility/references/sources.md)
- [Promotion](skills/seo-authority-promotion/references/sources.md)
- [Specializations](skills/seo-specializations/references/sources.md)
- [Donor/update policy](skills/seo-aieo/references/donor-policy.md)

Google/Bing/Яндекс/OpenAI/Hermes official links в этих материалах — первоисточники продуктовых правил с явно ограниченным scope. Наличие документированного UI не доказывает API, права конкретного аккаунта или фактические результаты. Перед production decision проверяйте текущий первоисточник и состояние аккаунта отдельно.

## Что намеренно исключено

Частные case histories, raw audits/client exports, исходные исследовательские вложения, сырые audit/review logs, account lists, credential paths/values и персональные runtime roots не являются частью пакета. Локальные ссылки на них заменены переносимой документацией/переменными, а не несуществующими файлами внутри repo. Читаемый отчёт подготовки, hashes/diff и реальные test logs хранятся отдельно у владельца; не требуются для runtime.
