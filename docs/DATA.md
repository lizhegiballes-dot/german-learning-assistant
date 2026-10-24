# Dictionary coverage and data storage

## Dictionary coverage, honestly

| Source | Included content | License / limits |
| --- | --- | --- |
| EEA / Eionet GEMET 4.2.3 | 5,352 German concepts with English and/or Chinese labels | CC BY 4.0. Environmental and related specialist terminology; labels, not a comprehensive learner dictionary. |
| HanDeDict contributors | 233,624 German-to-Chinese **reverse exact-match rows** | CC BY-SA 3.0 for the bundled snapshot. These are rows, **not unique German headwords**. A reversed Chinese-German dictionary can be ambiguous; every result is marked as reference content. |
| English Wiktionary contributors | Optional, requested German-section definitions in English | CC BY-SA 4.0. Disabled by default. Selected words are sent to the public API; definitions are then kept locally. Availability and coverage can vary. |

Missing Chinese definitions are shown as missing, or with an explicitly labeled English fallback. **No machine-generated Chinese meaning is silently invented.** This release does not promise a complete German dictionary, complete inflection analysis or exhaustive senses. The online parser simplifies wiki markup; the original entry and contributor history remain linked for checking.

Duden / Langenscheidt definitions, recordings, private course materials and personal study histories are **not bundled**. WortGlide is independent and is not endorsed by any dictionary publisher. See [attributions and transformations](../THIRD_PARTY_NOTICES.md).

## Your data

Learning data lives in **IndexedDB belonging to this extension in your current Chrome profile**. Preferences live in chrome.storage.local. It is not automatically stored in Documents, a desktop folder, another browser profile or another computer. Use Settings → Backup JSON to create a file in your chosen download location; that file can be backed up to your own drive.

The extension stores the reading page's **origin and path** with a lookup, locally, to help preserve reading context. Query strings and fragments are removed. Paths can still contain private identifiers: treat your backups as private. Browser storage is not an encrypted vault, and uninstalling the extension removes its storage. JSON backup is the restore format; CSV and TSV are portable word lists, not full backups.

Online mode contacts only English Wiktionary; the selected word, ordinary connection metadata and your IP address reach that service. Reading URLs, collections and the wordbook are not included in those requests. No cloud sync is provided. Browser-managed page translation, system features and Chrome account behavior are outside this extension's control. [Full privacy policy](../PRIVACY.md).

