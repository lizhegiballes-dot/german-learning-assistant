# WortGlide
### Your German Reading Companion

**Select a word. Keep your flow.**

Turn everyday German reading into a wordbook that grows with you. Quick selection lookup, daily collections, simple review and one-click exports — right in your browser.

[**Download for Chrome →**](https://github.com/lizhegiballes-dot/wortglide/releases/latest) · [中文说明](README.zh-CN.md) · [Getting started](#get-started)

![WortGlide — German words, collected your way](docs/wordbook.png)

## Less friction. More German.

| While you read | Make it yours |
| --- | --- |
| **Look up in place** — select a word or use the right-click menu. | **Build collections** — one for a book, a course or a new interest. |
| **Keep your reading flow** — definitions and local German pronunciation beside the word. | **Find it by day** — today's words, in the order you met them. |
| **Know what keeps coming back** — one word record, with a lookup count. | **Take it anywhere** — one-click CSV and Anki exports, plus portable JSON backups. |

English-first, with a Chinese interface option and separate English / Chinese definition preferences. Your notes, collections and review progress stay on your device. No account or desktop service needed.

## Get started

1. [Download the latest extension ZIP](https://github.com/lizhegiballes-dot/wortglide/releases/latest) and extract it to a folder you will keep.
2. Open Chrome's extensions page, enable **Developer mode**, then choose **Load unpacked**.
3. Select the folder that directly contains **manifest.json**. In a source checkout, select **extension**.
4. Open WortGlide from your toolbar, set your preferences and refresh your reading tabs.

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
