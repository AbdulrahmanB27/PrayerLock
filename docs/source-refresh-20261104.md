# Current app alignment review — November 4, 2026

Read-only product and policy review for the website and launch-film refresh. This review does not establish physical-device notification delivery, location accuracy, compass accuracy, or restriction enforcement. It made no edits to the supplied Android project.

## Source and comparison

- Current configured project: `App/prayerlock`; authoritative production source: `App/prayerlock/app/src/main`.
- Supplied `App/prayerlock.zip` is dated November 4 at 15:21; the extracted project is dated 15:21. All 91 production files in the configured source tree match their corresponding archive entries byte for byte.
- The archive additionally contains four old drawable files under `app/app/src/main/res/drawable`. These nested files differ from the configured root drawables. They are export artifacts, not the app module's current resources; do not use them for website identity assets.
- Baseline: `Website/tools/capture/refresh-20261103/source-hashes-before.json`, with the preserved project at `%TEMP%/PrayerLock-web-current-20261103`. The preserved project matches all 81 baseline production hashes.
- Current: 91 main files. Compared with the baseline, 18 changed, 10 were added, and none were removed. Build configuration and the theme/icon resources are unchanged.
- Current identity remains PrayerLock, application ID `com.prayerlockapp`, version `1.1` / code `2`, minimum SDK 24, target SDK 36 (`App/prayerlock/app/build.gradle.kts:14`). This source identity does not establish Google Play publication.

Android references below are relative to `App/prayerlock/app/src/main` and refer to this export. Later exports can move the line numbers.

## Changes worth reflecting in the website and film

| Area | November 4 behavior | Source references |
| --- | --- | --- |
| Reminder before Adhan | New optional notification, off by default. Default lead time is 5 minutes; the UI offers 5, 10, 15, 20, or 30 minutes. The source schedules a separate reminder and opens the app when tapped. This is a reminder control, not evidence of guaranteed background delivery. | `MainActivity.kt:1892`, `:9169`, `:9249`, `:12743`, `:12834`; `PrayerLockAlarmReceiver.kt:19` |
| Adhkar Hadith details | New expandable Hadith section with Arabic narration, English narration in English mode, and a localized citation. Tapping the citation copies it to the system clipboard. All 26 built-in data entries have bilingual citation/narration fields. This review confirms the content and UI exist; it does not independently authenticate the citations or translations. | `AdhkarTab.kt:398`, `:404`, `:450`, `:467`, `:479`; `AdhkarData.kt:13`, `:55` |
| Qibla heading | Heading now uses the corresponding cardinal direction, N/NE/E/etc., or its Arabic label, instead of always appending N. | `MainActivity.kt:7085` |
| Compass calibration | New figure-eight animation with a moving phone and trail. Sensor orientation and magnetic-declination code were not changed by this export. Do not describe the visual change as a new compass-accuracy guarantee. | `MainActivity.kt:6500`, `:7519`, `:7535` |
| Home sky illustration | Sun and moon now move vertically at a fixed horizontal position opposite the text. The canvas mirrors in Arabic; the moon uses the current lunar phase. The prior export's East-to-West arc/no-RTL-mirroring description is obsolete. | `MainActivity.kt:4791`, `:4800`, `:4814`, `:4845`, `:4934`, `:4995` |
| Home-screen widgets | Six registered variants now exist. Three additions are Current & Next Prayer, Current Prayer Sky, and Next Prayer Slim, alongside Prayer Schedule, Prayer Compact, and Focus Block. Existing variants also have revised presentation/localization. | `AndroidManifest.xml:89`, `:132`, `:145`, `:158`; `res/values/strings.xml:3`; `PrayerDualWidgetProvider.kt:66`; `PrayerSkyCurrentWidgetProvider.kt:194`; `PrayerSlimNextWidgetProvider.kt:72` |
| Arabic coverage | Added Arabic disclosure/permission UI, native privacy text, many configuration and management dialogs, notifications, and calculation-method names. Some source strings remain English. Describe English/Arabic support without claiming every screen or system dialog is completely translated. | `MainActivity.kt:755`, `:822`, `:8056`, `:8840`, `:11305`, `:12834`; `LanguageManager.kt:127` |
| Product wording | The active banner now says PRAYER BLOCK ACTIVE / حظر الصلاة نشط. Several former shield labels became block labels. Arabic Iqamah wording now explicitly describes the delay between Adhan and starting the block. | `MainActivity.kt:3315`, `:9289`, `:9306`; `LanguageManager.kt:267` |

The broader feature set from the November 3 review remains: five daily prayers, optional Sunrise and Last Third of the Night entries/reminders, local timetable adjustments, calculation methods, per-prayer Adhan voices, Iqamah delay, Qibla, Adhkar counters, six Arabic font choices, Tasbeeh groups, focus sessions, schedules, and travel settings. These should not all be presented as newly added on November 4.

## Icon and lighter-screen direction

- The current transparent brand symbol is `res/drawable/ic_prayerlock_transparent.xml:1`. It has a 68 × 68 viewport, a group translated by `(-20, -12.5)`, and two paths: cream `#F4F0E6` with even-odd fill, and mint `#9BCDC7`. It has no background path or clock tick marks.
- The adaptive launcher foreground is a different presentation of the same paths: a 108 × 108 viewport, scale `0.65` around `(54,54)`, translated down `5` (`res/drawable/ic_launcher_foreground.xml:7`). Keep the transparent symbol's own geometry for the “A moment for prayer” illustration.
- At review start, the focus illustration still used a hand-drawn substitute SVG (`Website/index.html:173`; `Website/ar/index.html` matching section). Replace it with the source-derived transparent symbol, preserving the circular illustration around it.
- Theme resources have not changed since November 3. `ui/theme/Theme.kt:9` still uses one `darkColorScheme`; the `darkTheme` argument does not select a separate light scheme (`:25`). Do not label native screenshots as a new light mode.
- Favor authentic Dhuhr and Asr daytime sky captures in hero, poster, feature frames, and film. Keep Fajr/Maghrib/Isha where demonstrating the day cycle. Qibla, Adhkar, and Settings remain native darker surfaces; brightening their pixels would misrepresent the app.

## Existing EN/AR copy that needs attention

1. Arabic `Website/ar/index.html:349` explicitly says there are three widgets. Current source has six. Suggested replacement: “أبقِ جدول الصلاة والصلاة الحالية والقادمة على شاشتك الرئيسية، مع ست أدوات تناسب مساحتك.” English `Website/index.html:349` names only the older three types; broaden it to the full set or say “six home-screen widgets.”
2. `Website/index.html:320` and `Website/ar/index.html:320` still call the block capture a prayer shield / درع الصلاة. Prefer “prayer focus window” / “فترة التركيز للصلاة” or match the new visible Prayer Block wording. The asset filename can remain `prayer-shield.png` for compatibility.
3. English Adhkar's optional transliteration and translation claim remains defensible (`AdhkarTab.kt:363`). Arabic continues to suppress both; do not reintroduce the old Latin-transliteration claim (`:364`, `:467`). Add Hadith details to either locale only when the delivered capture actually shows them.
4. The existing five-sky selector remains defensible. Any text explaining physical East-to-West screen motion or identical LTR/RTL geometry would now be stale. “A sky that changes with your day” remains exact.
5. Existing six-font, optional supplementary-time, Iqamah, travel-setting, and local-timetable claims remain supported. Do not present travel mode as determining a user's religious entitlement to combine/shorten prayers; reviewed code skips Asr/Isha triggers while the setting is active (`MainActivity.kt:2361`, `:7476`).
6. Keep “Coming soon to Google Play” until a public listing/release is verified. Keep modest focus/reminder language rather than guaranteed automatic blocking.

## Compact source-supported copy

English:

- “A little time to prepare. Choose an optional reminder 5, 10, 15, 20, or 30 minutes before Adhan.”
- “Read with context. Open Hadith details beside your Adhkar and tap a citation to copy it.”
- “Close at hand. Six home-screen widgets keep your timetable, current prayer, next prayer, or focus control within reach.”
- “English or Arabic. Prayer names, times, counters, and Adhkar in your language.”
- “A sky that changes with your day.”

Arabic:

- “وقت للاستعداد. اختر تنبيهًا اختياريًا قبل الأذان بخمس أو عشر أو خمس عشرة أو عشرين أو ثلاثين دقيقة.”
- “اقرأ الذكر مع سياقه. افتح تفاصيل الحديث بجانب الأذكار، واضغط على المرجع لنسخه.”
- “في متناولك. ست أدوات للشاشة الرئيسية تُبقي جدولك والصلاة الحالية والقادمة والتحكم بالتركيز قريبًا منك.”
- “بالعربية أو الإنجليزية. أسماء الصلوات والأوقات والعدّادات والأذكار بلغتك.”
- “سماء تتغيّر مع يومك.”

## Native policy and public-policy alignment

The English native policy's four substantive blocks and effective date are unchanged from November 3. Normalized English native/public comparison passes 4/4: strip HTML from the public page, decode entities, normalize whitespace and Kotlin newline escapes, and omit bullet glyphs. The effective date remains **January 1, 2024**, not the export or website-refresh date (`MainActivity.kt:8079`).

Exact raw Kotlin English-value SHA-256 hashes, including literal newline escapes in the permissions value:

| Value | SHA-256 |
| --- | --- |
| Effective date | `a62ffa32bcb0457f33fb8819601bedb95d674a61b642fc3053fbc988ab981f33` |
| Section 1 | `dbeb44252ecfcd73ebf9a267f27a0b9e50c853bf66d9d7c1177043a22da30a29` |
| Section 2 | `9973271b9d3cb193b5505fde0f191682af7d75d8ab53fe1aefa4938425c875ad` |
| Section 3 | `07b4db148a81f04f511767ab83fd7d1ffc1c12d0898d5fa382af1900c3ec1dda` |
| Section 4 | `aaa1bda33b9a899f854e40788b2eecc811d95b3e16964d4d3a09ef921e609308` |

The Arabic native policy is newly added (`MainActivity.kt:8056`–`:8156`). It is an abbreviated adaptation, not exact text parity with the English native policy or the current fuller public Arabic translation. In particular, its permissions block omits the Android Geocoder network-provider caveat and the English mention of interval windows. Its local-storage paragraph omits SharedPreferences. Preserve the fuller public Arabic translation of the unchanged English policy when maintaining congruent public EN/AR disclosures; do not silently remove the network caveat during this source refresh.

### Newly added native Arabic policy text, copied from source

**سياسة الخصوصية**

**تاريخ السريان: ١ يناير ٢٠٢٤**

**١. جمع البيانات واستخدامها**

صُمم تطبيق قفل الصلاة ليكون قائماً على الخصوصية أولاً. نحن لا نجمع أو نرسل أو نخزن أي بيانات شخصية أو إحصائيات استخدام خارج جهازك. جميع الوظائف، بما في ذلك حساب مواقيت الصلاة، ومؤقتات القفل، والتعديلات الجغرافية، تتم بالكامل محلياً على هاتفك.

**٢. الأذونات**

ليعمل التطبيق بالشكل المطلوب، يستخدم الأذونات التالية:

- الموقع الجغرافي: يُستخدم محلياً لحساب مواقيت الصلاة بدقة، واتجاه القبلة، ونطاقات القفل أو المساجد الاختيارية.
- الظهور فوق التطبيقات الأخرى: يُستخدم حصرياً لعرض شاشة تذكير وقفل الصلاة بملء الشاشة أثناء أوقات الصلاة. نحن لا نقرأ محتوى الشاشة أو الرسائل الشخصية.
- قائمة التطبيقات: تُستخدم محلياً فقط لتتمكن من اختيار التطبيقات المستثناة أو المحظورة أثناء فترات الصلاة أو التحصين. قائمة تطبيقاتك لا تغادر جهازك أبداً.
- الإشعارات والتنبيهات والصوت: تُستخدم لتشغيل تذكيرات الصلاة الدقيقة، وصوت الأذان، ووضع الاهتزاز في المسجد.

**٣. التخزين المحلي**

يتم حفظ جميع جداولك وتفضيلاتك محلياً على جهازك فقط. لا يدير التطبيق أي خوادم خارجية للتحليلات أو التتبع.

**٤. التغييرات على هذه السياسة**

قد نقوم بتحديث سياسة الخصوصية من وقت لآخر لتعكس تحديثات التطبيق وميزاته الجديدة. ستكون أي تحديثات متاحة داخل التطبيق.

### Publication-relevant limits rechecked in this export

- The manifest still declares `INTERNET` and `allowBackup="true"` (`AndroidManifest.xml:8`, `:23`). Geocoder calls remain. Do not add a blanket marketing promise that nothing ever leaves the device; the unchanged English policy itself acknowledges network geocoding.
- Both backup XMLs include shared preferences generally and exclude `prayer_lock_prefs.xml`; the separate `adhkar_prefs` store remains outside that exclusion (`res/xml/backup_rules.xml:10`; `res/xml/data_extraction_rules.xml:9`; `AdhkarData.kt:20`). Policy text parity does not establish a universal no-backup/no-transfer claim.
- The manifest still registers no accessibility service and declares no `SYSTEM_ALERT_WINDOW`. `MainActivity.kt:658` hardcodes the grant states to true. `LockoutOverlayService.kt:491` returns true from its accessibility check; `:513`–`:526` retains the default kickout-only early return. Refreshed screenshots are presentation evidence, not proof of reliable automatic app blocking.
- NFC remains declared and locally handled, while its normal Settings item is still deliberately hidden (`MainActivity.kt:8764`). Do not feature NFC as a normal available product control.
- Both native online-policy actions still point to the homepage, not `/privacy/` (`MainActivity.kt:8179`, `:8315`). The public site's dedicated policy links remain the right publication destination.

## Review scope and integrity

Only this documentation file was written by the alignment review. No Android source, HTML, CSS, media, or privacy page was changed by this review. Capture and website owners should attach their own current-run build, screenshot, responsive-layout, media, and deployment verification evidence.
