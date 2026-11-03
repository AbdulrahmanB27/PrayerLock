# Current app alignment review — November 3, 2026

Read-only review of the supplied Android export for the website and launch film refresh. This is a product-content review, not an Android release audit. No Android files or privacy-policy pages were changed by this review.

## Source and comparison

- Authoritative current project: `App/prayerlock`. `App/prayerlock.zip` is dated November 3 at 18:06, and the extracted tree is dated 18:07. There is no second `App/app` project in the current workspace.
- Compared current `app/src/main` against `PlayStore/source/capture/arabic-20261103/source-hashes-before.json` and the preserved matching project at `%TEMP%/PrayerLock-ar-capture-20261103`.
- Baseline: 80 production main files. Current: 81. Of the baseline paths, 13 changed and 10 launcher `.webp` files were removed; 11 paths were added (10 `.png` launcher files and `ic_prayerlock_transparent.xml`).
- Changed Kotlin files: `MainActivity.kt`, `AdhkarTab.kt`, `LanguageManager.kt`, `LockoutOverlayService.kt`, `PrayerLockAlarmReceiver.kt`, and `ui/theme/Type.kt`.
- The manifest and six vector/adaptive-icon files also changed. Existing screenshots and film predate this export; a same-day Arabic capture is still stale relative to this evening export.
- Current identity is `PrayerLock`, application ID `com.prayerlockapp`, version `1.1` / version code `2`, minimum SDK 24, target SDK 36 (`App/prayerlock/app/build.gradle.kts:14`). The morning build was `com.aistudio.prayerlock.abcde`, version `1.0` / code `1`. Minimum and target SDKs did not change.

All Android references below are relative to `App/prayerlock/app/src/main` and refer to the reviewed export; line numbers can move in later exports.

## Feature changes relevant to the website

| Area | Existing behavior in morning capture | Current behavior and source |
| --- | --- | --- |
| Sunrise | Always included as the sixth timetable row | Optional home row, default off. Independently optional notification with no lockout. `MainActivity.kt:1853`, `:5318`, `:8661`, `:8756` |
| Last Third of the Night | No corresponding row or notification | Optional home row and optional Tahajjud reminder, default off. No screen lock. Calculation uses the final third of the Maghrib-to-next-Fajr interval. `MainActivity.kt:1868`, `:3620`, `:5326`, `:8826`, `:8859`, `:12309`; `PrayerLockAlarmReceiver.kt:20` |
| Home sky | Prayer-specific sky palettes | Continuous interpolation between prayer palettes, including a transition toward Fajr during the final 50 minutes before Fajr. `MainActivity.kt:2640`, `:3626`, `:3640` |
| Celestial scene | Existing sun/moon illustration | Reworked East-to-West motion in an upper sky arc; explicit avoidance of RTL mirroring so sun/moon direction is the same in both languages. `MainActivity.kt:4745` onwards |
| Floating controls | Existing dashboard and navigation | More opaque floating shield-status and bottom-navigation pills; Arabic status and action labels. `MainActivity.kt:3238`, `:3268`, `:3321` |
| Arabic UI | Partial Arabic strings; English elements remained | Much broader localization of prayer names, digits, formatted times, voices, locations, quick actions, Qibla, settings, and overlays. English and Arabic remain the only selectable languages. `LanguageManager.kt:5`, `:36`, `:65`, `:75`, `:100`; `MainActivity.kt:1207`, `:1216` |
| Arabic Adhkar | Same phonetics/English translation controls and English category text as English view | Arabic categories, page/repetition counts, and controls. Both transliteration and English translation are intentionally hidden in Arabic mode, and the phonetics toggle is absent. English mode retains the optional transliteration/translation view. `AdhkarTab.kt:59`, `:107`, `:162`, `:187`, `:358`, `:578` |
| Adhkar layout | “SPIRITUAL REMEMBRANCE” eyebrow and required/optional text badge | Eyebrow removed; larger reading area/bottom space; fixed dot marks requirement status with a tooltip. `AdhkarTab.kt:132`, `:310`, `:398` |
| Arabic font | Six existing font choices, default Scheherazade | Same six choices; default changes to Noto Naskh, with a new persisted preference key `selected_arabic_font_v2`. `ui/theme/Type.kt:65`, `:123` |
| Audio controls | Per-prayer sound profiles, custom audio, silent override existed | Per-prayer silent override now defaults to false rather than true. Explicit hardware screen/volume-change muting paths and additional deduplication/off-schedule alarm handling are present. These require device verification before promising reliable hardware-button behavior. `MainActivity.kt:113`, `:11559`; `PrayerLockAlarmReceiver.kt:130` |
| App picker | Previously populated from already-selected packages only | Current code queries launchable installed apps and preserves previous selections; manifest now has launcher `<queries>`. This establishes selection UI, not reliable restriction enforcement. `MainActivity.kt:13303`; `AndroidManifest.xml:16` |

## Existing features worth showing without describing them as newly added

- Iqamah delay: persisted setting, 0–30-minute slider in 5-minute steps, with a distinct Iqamah countdown. `MainActivity.kt:1480`, `:5189`, `:8891`–`:8916`.
- Prayer calculation method, per-prayer minute offsets, per-prayer Adhan voices, custom audio, and optional Dua after Adhan. `MainActivity.kt:5612`, `:5621`, `:8563`, `:8940`, `:8993`.
- Tasbeeh unlock and configurable named Dhikr groups/targets already existed. Current UI translates them into Arabic and accepts Arabic digits for targets. `MainActivity.kt:213`, `:1777`, `:9279`, `:9326`, `:9374`–`:9421`.
- Haptic feedback switch already existed. Current dashboard helper reads the persisted toggle; current setting is localized. `MainActivity.kt:1969`–`:1981`, `:10232`–`:10247`.
- Qibla compass with active location, location/calibration controls, and travel toggle already existed. Current labels are localized. `MainActivity.kt:6180`, `:7050`, `:7307`, `:7344`.
- Travel mode is described in-app as “Jam' & Qasr”. The reviewed scheduling code skips Asr and Isha triggers while active. Describe a travel setting; do not imply that the app determines a user's religious entitlement to shortened/combined prayer or physically performs the prayer. `MainActivity.kt:2336`, `:7344`–`:7352`.
- Manual focus, focus schedules, weekly breaks, exemption pause, reminder controls, and supplementary home-screen widgets remain present. The visible dashboard has Home, Qibla, Adhkar, and Settings. `LogsHistoryScreen` remains in source but is not a dashboard tab (`MainActivity.kt:2820`, `:10496`).
- Six font choices and required-Adhkar configuration already existed. The current required-items picker explains that all Adhkar remain visible, while only selected ones count toward Tahseen completion. `AdhkarTab.kt:875`, `:977`.
- NFC logic remains in source, but its settings item is deliberately commented out with “hide it from the UI for now.” Do not feature NFC as a normal available product control (`MainActivity.kt:8477`–`:8529`).

## Current identity and visual assets

- The dark charcoal gradient background, cream lock/mosque shape, and mint clock hand remain the identity.
- The current adaptive launcher foreground contains a group scaled to `0.65`, pivoted at `(54,54)`, translated down `5`; it contains the lock silhouette and clock hand without the old clock tick marks (`res/drawable/ic_launcher_foreground.xml:7`).
- `Website/assets/images/app-icon.svg` was the older full-size untransformed symbol with clock ticks at review start. The current source also provides `ic_prayerlock_transparent.xml` and updated lock/stat/monochrome vectors.
- Refresh all five home skies, Qibla, Adhkar, prayer shield, the home-sky GIF, Adhkar GIFs, and film/poster from the current source. If an image shows Sunrise/Last Third, state that they are optional and record the settings used for that capture.
- A useful compact extra capture is Settings → Prayer Times & Audio with the supplementary times, Iqamah, and tuning controls; a second can show Tasbeeh groups/fonts. Static screen captures do not verify notification delivery, sensors, permission grants, or enforcement.

## Website text that needs changing

At the start of this review:

1. `Website/ar/index.html:295`–`:296` describe the Arabic Adhkar image as including Latin transliteration and translation. Current Arabic mode intentionally hides both.
2. `Website/ar/index.html:312` says “اقرأ أذكارك مع كتابتها بالأحرف اللاتينية وعدد مرات التكرار.” Replace the Latin-transliteration claim with Arabic reading and localized repetition counts. Example: “اقرأ أذكارك بالعربية، واختر الخط الذي يناسبك، وتابع عدد مرات التكرار.”
3. `Website/ar/index.html:383` says the current film is English with Arabic subtitles and that some app UI remains English. Refresh the film description to match the actual delivered media. Broader Arabic localization is now source-confirmed, but onboarding, native privacy, and some dialogs still contain English, so do not claim every single screen is completely translated.
4. `Website/index.html:180` and `Website/ar/index.html:181` describe five discrete prayer skies. This remains a defensible poetic description, but the app now blends smoothly across the day. “A sky that changes with your day” is more exact.
5. The existing main feature copy is generally modest and compatible: prayer timetable, reminders, Qibla, Adhkar, calculation methods, offsets, Adhan selection, and focus sessions. The refreshed showcase can expose supplementary times, Iqamah, fonts, and localized counters without claiming new enforcement strength.
6. Keep “Coming soon to Google Play” unless the owner provides/verifies a public release listing. The application ID change alone does not establish store publication.

## Defensible compact showcase copy

These describe source-visible features and controls without a release-reliability guarantee:

- “Beyond the five daily prayers. Add Sunrise and the Last Third of the Night to your home screen, with optional reminders that don't start a lockout.”
- “Set your own pace. Tune prayer times to your local timetable, set an Iqamah delay, and choose an Adhan voice for each prayer.”
- “Remembrance, your way. Choose an Arabic font, set Tasbeeh groups and repetition targets, and adjust touch feedback.”
- “English or Arabic. Localized prayer names, times and counters, with an Arabic reading view for your Adhkar.”
- “Direction for the journey. A Qibla compass with location, calibration and travel settings.”

Arabic options:

- “إلى جانب الصلوات الخمس. أضف الشروق والثلث الأخير من الليل إلى الشاشة الرئيسية، مع تنبيهات اختيارية لا تُفعّل قفل الشاشة.”
- “على إيقاع يومك. اضبط مواقيت الصلاة لتوافق جدول مسجدك، وحدّد تأخير الإقامة، واختر صوت الأذان لكل صلاة.”
- “أذكارك بطريقتك. اختر الخط العربي، وخصّص مجموعات التسبيح وعدد التكرارات، واضبط الاهتزاز التفاعلي.”
- “بالعربية أو الإنجليزية. أسماء الصلوات والأوقات والعدّادات بلغتك، مع عرض عربي لقراءة الأذكار.”
- “وجهتك أثناء السفر. بوصلة قبلة مع إعدادات الموقع والمعايرة ووضع السفر.”

## Privacy policy extraction and parity

The current native policy is `MainActivity.kt:7788`–`:7875`. Its four substantive sections and effective date are unchanged from the preserved morning project. After stripping HTML, unescaping entities, normalizing whitespace, replacing Kotlin `\n` sequences with spaces, and omitting bullet glyphs, all four text blocks match `Website/privacy/index.html` (4/4). The Arabic page remains a translation of those same sections; its date remains January 1, 2024. No new policy content or effective date was warranted by a source-sync task.

SHA-256 values below hash each exact raw Kotlin `text = "..."` value as UTF-8 (the permission value retains literal `\n` escapes):

| Value | SHA-256 |
| --- | --- |
| Effective date | `a62ffa32bcb0457f33fb8819601bedb95d674a61b642fc3053fbc988ab981f33` |
| Section 1 paragraph | `dbeb44252ecfcd73ebf9a267f27a0b9e50c853bf66d9d7c1177043a22da30a29` |
| Section 2 body | `9973271b9d3cb193b5505fde0f191682af7d75d8ab53fe1aefa4938425c875ad` |
| Section 3 paragraph | `07b4db148a81f04f511767ab83fd7d1ffc1c12d0898d5fa382af1900c3ec1dda` |
| Section 4 paragraph | `aaa1bda33b9a899f854e40788b2eecc811d95b3e16964d4d3a09ef921e609308` |

### Complete current native policy text

**Privacy Policy**

**Effective Date: January 1, 2024**

**1. Data Collection and Usage**

PrayerLock is designed to be privacy-first. We do not collect, transmit, or store any personal data, usage stats, or tracking metrics off your device. All functions, including the calculation of prayer times, lockout timers, and geographical adjustments, are performed entirely locally on your phone.

**2. Permissions**

To function as intended, PrayerLock uses the following permissions:

- Location & Geocoding: Used locally to calculate accurate prayer times, Qibla direction, and optional geofenced lockout/Masjid zones. When you search for a city or resolve a GPS coordinate label, Android's Geocoder service may query network geocoding providers.
- Draw Over Other Apps: Used exclusively to display the full-screen focus lockout reminder during prayer times. We do not read screen contents, keystrokes, or personal messages.
- App Visibility (`<queries>`): Used strictly on-device so you can choose which launchable apps are exempted or restricted during prayer/Tahseen/interval windows. Your app list never leaves your device.
- Notifications, Alarms & Audio/DND: Used to trigger exact prayer reminders, Adhan audio, and optional Masjid vibrate mode.

**3. Local Storage**

All your schedules and preferences are stored on your device using Android SharedPreferences. PrayerLock does not operate any remote analytics or tracking servers.

**4. Changes to This Policy**

We may update our Privacy Policy occasionally to reflect app updates and features. Any updates will be available within the app.

The current dialog adds “View Online” and “Close” actions. Its online action and Settings privacy URL both point to `https://abdulrahmanb27.github.io/PrayerLock/`, the homepage rather than `/privacy/` (`MainActivity.kt:7889`, `:8030`). The public website itself links to its dedicated policy correctly.

### Publication-relevant limits, confirmed against this export

- Continue using modest “focus session” / “reminder” language. Current `MyAccessibilityService.kt` is a placeholder; the manifest registers no accessibility service and declares no `SYSTEM_ALERT_WINDOW`. `MainActivity.kt:658`–`:659` hardcodes those grant states to true. `LockoutOverlayService.kt:491` returns true from its accessibility check, and `:513`–`:526` takes a default kickout-only early return without adding an overlay. Its remaining `:533` overlay-window path does not establish a permission grant. Reliable automatic blocking remains unverified; fresh Compose images cannot establish it.
- Do not add a blanket “nothing ever leaves your device” marketing claim. Policy section 2 acknowledges Android network geocoding; source Geocoder paths remain. `INTERNET` remains in the manifest. The policy's section 1 entirely-local wording is unchanged and still broader than this implementation evidence.
- `android:allowBackup="true"` remains. Both backup XMLs include shared preferences generally and exclude `prayer_lock_prefs.xml`; separate `adhkar_prefs` stores optional-item IDs/font choices and is not excluded. Exact policy parity does not prove a universal no-backup/no-transfer promise.
- NFC remains declared and locally handled, but hidden in UI. Prayer logs and saved location/configuration data remain local source concepts. The current policy is the supplied app text; this review does not replace it with a newly authored legal policy.

The source review made no Android edits and did not claim a physical-device notification, compass, location, or lockout test.
