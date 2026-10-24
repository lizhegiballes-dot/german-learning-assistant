# Architecture

WortGlide is a standalone Manifest V3 extension. There is no desktop service or application backend.

- content.js observes user selections outside editing fields, creates a closed-shadow popup and sends internal extension messages. It does not scrape an entire page. Generation / request checks keep late responses from reopening a closed card or replacing another word.
- background.js owns lookup request IDs, provider jobs, message validation, user preferences, local-only TTS and context menus.
- dictionary.js lazily loads GEMET, then HanDeDict when Chinese reference lookup is needed. Optional online lookup uses only the English Wiktionary German section. It limits pending requests, rate, response size and timeout, with a cooldown after HTTP 429.
- storage.js uses IndexedDB transactions for words, lookup events and collections. The event ID is the idempotency key. Background enrichment merges definitions without creating a new lookup event. Dictionary redirects can reconcile canonical headwords; conservative normalization is not a complete German lemmatizer.
- app.js provides daily / collection views, notes, export, review and settings. export.js produces CSV with spreadsheet-formula protection and text-only Anki TSV, retaining source / license metadata.
- i18n.js contains English and Chinese UI strings. Dictionary language is a separate preference.

## Storage and recovery

The database is scoped to a Chrome profile and extension ID. Preferences use chrome.storage.local. Uninstalling the extension removes this browser-owned storage. No portable desktop folder or shared server is created automatically.

A JSON backup includes events, words, collections, review, notes and settings. Validation happens before the write transaction. Duplicate event IDs are ignored if they describe the same lookup and rejected if they conflict. Counts are rebuilt from merged events. Existing notes and review state win during a merge; a restore is not a destructive rollback.

Day grouping uses the user's local calendar date at lookup time, retained in each event. The daily list orders words by their first event on that day, while the all-lookups view sorts by latest lookup. Review is a small fixed interval schedule, not FSRS / Anki scheduling. CSV / TSV do not restore all study state.

## Rebuild dictionary assets

Use Python 3.10+ and independently obtained upstream source snapshots:

    python scripts/build_data.py --gemet path/to/gemet.rdf.gz --handedict path/to/handedict.u8 --out extension/data

GEMET source: https://www.eionet.europa.eu/gemet/en/exports/rdf/latest
HanDeDict source: https://github.com/gugray/HanDeDict

Preserve the original header and contributors, SHA-256, license, attribution and transformation statements. See THIRD_PARTY_NOTICES.md. The number of reverse-match rows is not a count of unique German entries.

## Checks

    npm test
    npm run test:browser
    npm run test:extension
    python scripts/package.py --check
    python scripts/package.py

The browser harness uses a synthetic HTTPS origin and a simulated Chrome messaging layer over real IndexedDB. It covers UI languages, lookup deduplication, collections, backup merges, malformed input, exports, review and page reopen persistence. The extension suite separately launches a temporary Chromium profile with the actual unpacked extension; existing browser profiles are never used. Development fixtures are not bundled into the extension ZIP.
