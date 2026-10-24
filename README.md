# German Learning Assistant
### Word Lookup, Wordbooks, Review & One-Click Export

**Select a word. Keep your flow.**

I got tired of interrupting my reading to look up German words on Duden—waiting for pages to load and dealing with ads. So I built **German Learning Assistant**, a free, open-source Chrome extension for looking up words, saving vocabulary, reviewing and exporting word lists for Anki. It supports English and Chinese, and keeps your learning records on your own device.

我受够了在杜登查词时碰到的广告、缓慢加载和来回切换页面，于是做了 **German Learning Assistant**，一款免费开源的 Chrome 德语学习助手。划词查询、收藏生词、分类整理、复习，再一键导出 Anki 词单；支持中英文，学习记录保存在自己的设备上。

[**Download for Chrome →**](https://github.com/lizhegiballes-dot/german-learning-assistant/releases/latest) · [中文说明](README.zh-CN.md) · [Getting started](#get-started)

![German vocabulary wordbook](docs/wordbook.png)

## Less friction. More German.

| While you read | Make it yours |
| --- | --- |
| **Look up in place** — select a word or use the right-click menu. | **Build collections** — one for a book, a course or a new interest. |
| **Keep your reading flow** — definitions and local German pronunciation beside the word. | **Find it by day** — today's words, in the order you met them. |
| **Know what keeps coming back** — one word record, with a lookup count. | **Take it anywhere** — one-click CSV and Anki exports, plus portable JSON backups. |

English-first, with a Chinese interface option and separate English / Chinese definition preferences. Your notes, collections and review progress stay on your device. No account or desktop service needed.

## Get started

1. [Download the latest extension ZIP](https://github.com/lizhegiballes-dot/german-learning-assistant/releases/latest) and extract it to a folder you will keep.
2. Open Chrome's extensions page, enable **Developer mode**, then choose **Load unpacked**.
3. Select the folder that directly contains **manifest.json**. In a source checkout, select **extension**.
4. Open the extension from your toolbar, set your preferences and refresh your reading tabs.

Choose a default collection before starting a book. New lookups will land there automatically; you can always organize them later. Use Review for a small daily practice session, or export your words to continue in Anki.

## Local by default, flexible when you need it

Learning records are stored in this extension's database in your current Chrome profile. **Backup JSON** creates a file you control, ready for your own backup drive. Back up before uninstalling or moving an unpacked extension. [Privacy details](PRIVACY.md).

The included dictionaries combine GEMET terminology and clearly labeled HanDeDict Chinese reference matches. Optional online English definitions come from English Wiktionary. Coverage varies, and a missing Chinese meaning is shown honestly with an English fallback when available. German pronunciation needs an installed local system voice. [Dictionary sources and coverage](docs/DATA.md).

## Build with us

Vanilla JavaScript, no application build step. Chrome 116+.

    npm install
    npm test
    npx playwright install chromium
    npm run test:browser
    npm run test:extension
    python scripts/package.py

Browser checks use synthetic records and isolated storage. The browser harness simulates Chrome messaging over real IndexedDB; the extension smoke suite loads the actual unpacked extension. [Architecture and data rebuild](docs/ARCHITECTURE.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md).

Application code: [MIT](LICENSE). Dictionary data keeps its own [attribution and licenses](THIRD_PARTY_NOTICES.md).
