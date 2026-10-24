# Getting started

[← Project overview](../README.md) · [中文说明](../README.zh-CN.md)

## Install in Chrome

1. [Download the ready-to-load v0.1.0 extension ZIP](https://github.com/lizhegiballes-dot/german-learning-assistant/releases/download/v0.1.0/wortglide-0.1.0.zip).
2. Extract it to a folder you intend to keep. Chrome loads the files from that folder.
3. Open `chrome://extensions/` and turn on **Developer mode**.
4. Choose **Load unpacked** and select the folder containing `manifest.json`.
5. Open the extension from the toolbar, then refresh the webpages where you want to look up words.

The installation ZIP is named `wortglide-0.1.0.zip`. The v0.1.0 interface also says **WortGlide**, the project's earlier name. The separate `wortglide-source-0.1.0.zip` is the application source; in that package, load its `extension` folder.

This is a standalone Chrome extension. It does not need Python, a desktop server, an account or a paid API key for everyday use. The current release is distributed through GitHub, rather than the Chrome Web Store.

## Your first lookup

1. Choose the interface language from the language selector. In **Settings**, choose **Definition language** separately.
2. If you want online English definitions when local entries are missing, enable **Allow online English definitions**. It is off by default.
3. On a supported HTTP or HTTPS page, select a German word. With **Show after selecting text** enabled, a word card appears. You can also select text and use the extension's right-click menu command.
4. Check the source shown with the definition. Save the word to your wordbook if you want to learn it.

Browser-internal pages and extension stores do not allow normal extension injection. Editing fields do not trigger automatic lookup. Built-in browser PDF viewers and other special pages may behave differently from ordinary webpages.

Local lookup is preferred. The bundled data focuses on terminology and Chinese reference matches; general English definitions often need the optional online source. Trying the dictionary headword can help with inflected forms.

## Collections and daily history

Create a collection for a book, course or topic. In **Settings → Save new lookups to**, choose it before you start reading. New lookup records will be assigned there. **History only** keeps lookups without assigning them to a collection.

Use **Today**, the date filter and the collection selector to revisit a reading session. Words on a selected day are ordered by the first time you looked them up that day. Repeated lookups of the same normalized headword increase its count; retries and definition enrichment do not create extra lookup events.

Add notes and use **Include in review** for a small daily review routine. Its intervals are 1, 3, 7, 14 and 30 days.

## Export to Anki or a spreadsheet

Filter the wordbook by date or collection, or select individual words. If words are selected, export uses the selection; otherwise it uses the current view.

| Format | Use |
| --- | --- |
| **CSV word list** | Open or import a portable word list in a spreadsheet |
| **Anki TSV** | Import a text word list in Anki and map its columns to your note fields |
| **Backup JSON** | Merge learning records, collections, notes, review progress and settings back into the extension |

Anki TSV contains German, English, Chinese, lookup count, first lookup, last lookup, personal note, and source/license information. Choose the fields you want when importing into Anki. This export does not create an APKG package or bundle images and audio.

Keep source and license information when sharing dictionary-derived word lists.

## Backup and update

Before upgrading, moving folders or changing browser profiles:

1. Open **Settings → Backup JSON** and keep the downloaded file somewhere you control.
2. For an unpacked-extension update, keep the same extension folder path. Replace its files with the updated extension files.
3. In `chrome://extensions/`, use **Reload** for the existing extension, then refresh your reading pages.
4. Check that your wordbook is present. Use **Restore backup** if needed.

Do not uninstall first: Chrome removes an extension's browser storage when it is uninstalled. Changing the extension's location or browser profile can also give it different storage.

Backup restore merges records. It is not a rollback that replaces the entire current library. Matching events are deduplicated; existing notes and review state are retained when records merge.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| No popup after selecting text | Refresh the page after installation, check **Show after selecting text**, and try an ordinary webpage outside an editing field |
| No English definition | Try the headword and enable optional online English definitions; coverage and service availability still vary |
| No Chinese definition | Chinese coverage is limited; an English fallback may be shown when available |
| No German pronunciation | Install a local German system voice; remote voices are not used |
| Empty export | Check the current date/collection filters and selection |
| No words after moving folders | Return to the original extension location/profile if possible, or restore your JSON backup |
| Online lookup fails | Local records remain available; retry later and check the source entry independently |

## Feedback

[Open an issue](https://github.com/lizhegiballes-dot/german-learning-assistant/issues/new) with the extension version, Chrome/OS version, query word and short reproduction steps. Include a sanitized screenshot when useful. Keep full wordbooks, backup files and private reading addresses out of public reports.

[Dictionary coverage](DATA.md) · [Privacy](../PRIVACY.md) · [Development](ARCHITECTURE.md)
