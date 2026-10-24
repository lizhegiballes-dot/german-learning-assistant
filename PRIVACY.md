# Privacy / 隐私

WortGlide 0.1.0 is a local-first browser extension. There is no account system, telemetry, advertising, analytics, project-operated backend or automatic cloud sync.

## Stored on this device

- IndexedDB: normalized headwords, dictionary text and source / license metadata, lookup events and counts, local calendar dates, collections, notes and review scheduling.
- chrome.storage.local: interface / definition languages, automatic popup and optional online preferences, default collection and ignored-host preferences.
- A lookup event can store its reading page's origin and path, truncated to 240 characters. Query strings and fragments are discarded. Paths may still reveal reading activity or identifiers; backups are private files.
- Data is scoped to the current Chrome profile and extension ID. It is not an encrypted vault. Uninstalling the extension removes its browser storage. A JSON export creates a user-managed file; no backup is automatically sent anywhere.

## Network

Online English lookup is **off by default**. When enabled and the selected definition language has no cached match, the normalized word is sent to https://en.wiktionary.org/w/api.php via HTTPS without credentials. That service sees the query and normal connection information, including the IP address. WortGlide does not send reading URLs, notes, categories, full page contents or the wordbook with this request. Rate limiting, response size limits and a timeout are applied. Source links open external sites only when clicked.

German pronunciation selects a voice Chrome identifies as **local**, and refuses remote voices. Availability depends on installed operating-system voices. The extension ships no audio recordings. Browser-level services and operating-system behavior are governed by their respective providers.

## Permissions

- Page content scripts on HTTP(S) pages: detect the user's selected text and show the local popup. Typing fields are excluded. Automatic popup can be disabled; Chrome's site-access controls can further restrict access.
- storage / unlimitedStorage: save learning data locally without requesting a project account.
- contextMenus: provide a user-triggered selection lookup command.
- tts: use installed local German voices.
- en.wiktionary.org host permission: support the opt-in dictionary request. Having this permission does not turn online mode on.

Browser internal pages, the Chrome Web Store and pages Chrome does not permit extensions to modify cannot show the selection popup. No cookies, browsing-history API, microphone, payment or localhost permissions are requested.

## Control and backup

Use Settings to turn online lookup or the automatic popup on/off. Export a JSON backup before uninstalling, changing profiles or relocating an unpacked extension. Restore merges events by ID, preserving existing records and preventing duplicate counts. CSV / TSV exports are word lists, not full restore files. Store and share backups deliberately: they can contain your reading paths and notes.

中文：学习记录与设置保存在当前 Chrome 用户资料的扩展数据库里，卸载前要自行导出 JSON 备份。本扩展不自动上传备份。联网默认关闭；开启后按需把查询词发给英文维基词典，对方能看到词和 IP 等连接信息，不会收到生词本或阅读页面地址。查询事件在本机保留页面域名及路径，路径也可能敏感，请勿把完整备份发到公开 issue。发音仅选择浏览器标为本地的德语声音。可关闭自动弹窗或利用 Chrome 的站点权限限制访问范围。
