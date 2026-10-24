# Third-party notices / 第三方资料许可

Application code: MIT, copyright 2026 lizhegiballes-dot and WortGlide contributors.
The following dictionary datasets remain separately licensed. No endorsement by their contributors or publishers is implied.

## EEA / Eionet GEMET 4.2.3

- Source and licensor: European Environment Agency / Eionet, GEMET contributors.
- Original: https://www.eionet.europa.eu/gemet/en/exports/rdf/latest
- License: **Creative Commons Attribution 4.0 International** — https://creativecommons.org/licenses/by/4.0/ ; legal text: https://creativecommons.org/licenses/by/4.0/legalcode
- Distributed file: data/gemet.json (extension/data/gemet.json in source).
- Changes: extracted German preferred / alternative labels and English / Chinese preferred labels from the complete SKOS RDF export; only concepts having a German label and at least one target label are retained. Removed RDF structure, other languages and concept relations. This is a transformed subset, not the complete GEMET release. Source SHA-256, version, attribution and transformation statement are preserved in the JSON meta object.
- Every displayed concept links to its original concept page. These are specialist terminology labels, not general-purpose definitions.

## HanDeDict

- Attribution: **HanDeDict contributors**; the original source header, named contributor list and licensing statement are preserved verbatim in data/handedict-attribution.txt.
- Source: https://github.com/gugray/HanDeDict
- License in the bundled source snapshot: **Creative Commons Attribution-ShareAlike 3.0 Unported** — https://creativecommons.org/licenses/by-sa/3.0/ ; legal text: https://creativecommons.org/licenses/by-sa/3.0/legalcode
- Distributed files: data/handedict.json and data/handedict-attribution.txt (under extension/ in source).
- Changes: reversed Chinese-to-German dictionary lines into exact German label → Chinese reference rows; extracted part-of-speech tags, separated comma-delimited synonyms, retained parenthetical context and deduplicated identical rows. Traditional / simplified Chinese from the source is retained. This transformed data is distributed under **CC BY-SA 3.0**, not MIT.
- The header's snapshot version and original SHA-256 are retained in the JSON metadata. An older upstream README describes a different license version; this distribution follows and preserves the actual bundled snapshot's CC BY-SA 3.0 header.
- A reverse match may have narrower or different meanings than a full German dictionary entry. Match rows are explicitly labeled as reference material.

## English Wiktionary (optional online lookup)

- Attribution: **English Wiktionary contributors**, linked separately for each returned German entry and its contributor history; revision ID is stored when supplied by the API.
- Source and licensing policy: https://en.wiktionary.org/wiki/Wiktionary:Copyrights
- This application uses text under **CC BY-SA 4.0**: https://creativecommons.org/licenses/by-sa/4.0/ ; legal text: https://creativecommons.org/licenses/by-sa/4.0/legalcode
- Changes: extracts English definition lines from the German language section; simplifies wiki links and supported templates, omits examples, quotation lines, media and unrelated language sections. This is an abbreviated presentation: check the linked original for full markup and context.
- No Wiktionary definitions are pre-bundled. Optional lookup fetches individual entries on demand and stores returned definitions in the user's own wordbook. Redistributed extracts must retain attribution, the source / history links, change statement and share-alike license.

## Exports and redistribution

CSV, Anki TSV and JSON retain per-entry source and licensing fields. Keep these when sharing dictionary content. Your personal notes and learning events are your content; the software license does not override dictionary licenses or give others rights to your private records.

No Duden or Langenscheidt text/audio, textbook material, scraped publisher database, external avatar or publisher brand asset is included. Pronunciation uses an available local German system voice through Chrome's TTS API; synthesized speech is not represented as a publisher recording.

中文：软件 MIT 许可与词库许可分别适用。汉德反向词库及联网获取的维基词典文本有署名、相同方式共享等要求，导出后再传播时应保留来源和许可字段。术语库、反查词库不能宣称是杜登完整版。
