# November 5, 2026 source review

The supplied Android project is `App/prayerlock`. The configured app module contains 91 files under `app/src/main`, all byte-for-byte matches for the corresponding entries in `App/prayerlock.zip`. The archive SHA-256 is `4b2787d9b961d2b8a63d96eaf32e8f601b713d5c5e3695bf08fca30b7fd18032`. Four additional archive entries under `app/app/src/main` sit outside the configured module's source tree.

The preserved November 4 build input in `%TEMP%/PrayerLock-web-current-20261104` matches all 91 November 4 hashes in `Website/tools/capture/refresh-20261104/source-hashes-before.json`. The November 5 app module has 10 changed production files, with the same set of file paths. The broader project inventory excluding build and IDE directories went from 176 to 179 files, with 11 changes and three additions. The additional change is the version bump in `app/build.gradle.kts`. The additions are reference PNGs under `public/assets/aistudio`, outside the app module's resource tree.

PrayerLock remains `com.prayerlockapp`, with minimum SDK 24 and target SDK 36. The version is now `1.2` with code `3`. The manifest, application name, transparent brand vector, launcher vectors, and Compose theme match the November 4 hashes. The bright Dhuhr and Asr views come from the native sky artwork. The source version establishes the identity of this export. Google Play publication is a separate check.

## What changed in the app

The references in this table are relative to `App/prayerlock/app/src/main`.

| Area | Source-supported change | References |
| --- | --- | --- |
| Navigation | Swipe horizontally between Home, Qibla and Adhkar, with the selected tab following the current page. Settings opens separately. | `MainActivity.kt:1239`, `:2726`, `:2735`, `:3403` |
| Home and location | The night sky uses a softer moon glow. The moon phase button moved from the Home header into the Location dialog, where it opens the existing lunar details. The location summary is flatter and the quick-city chips were removed. GPS and city search remain. | `MainActivity.kt:4315`, `:4438`, `:4509`, `:4547`, `:4966`, `:5219`, `:5235` |
| Qibla | The dial and control layout were redesigned. The dial displays the direction of prayer and the phone's compass heading. The calibration guide still animates a phone along a figure-eight, now with a solid path and a simplified visual treatment. This is a presentation change. | `MainActivity.kt:6687`, `:6992`, `:7050`, `:7432`, `:7492` |
| Adhkar | The in-tab `Aa` control now saves whether to display transliteration and English translation in `adhkar_prefs`. The English default remains on. The Arabic view still shows Arabic text and the repetition counter. Hadith content and citation behavior carry over from November 4. | `AdhkarTab.kt:67`, `:172`, `:372`; `AdhkarData.kt` |
| Widgets | The six registrations remain. Five prayer widget layouts have updated presentation. Prayer Schedule and Prayer Compact gain native sky backgrounds, and Prayer Compact's tall layout shows current prayer as well as the next-prayer countdown. The common bitmap renderer adds soft mist and sheen to the artwork. Focus Block remains the sixth variant. | `AndroidManifest.xml:89`–`:168`; `PrayerScheduleWidgetProvider.kt:337`; `PrayerTodayWidgetProvider.kt:209`, `:264`; `PrayerSkyCurrentWidgetProvider.kt:549`, `:623`; `res/layout/widget_{dual_prayer,schedule,sky_current,slim_next,today}.xml` |
| Supplementary times | The existing Sunrise and Last Third of the Night controls have simpler visual grouping in Settings. Their purpose and options carry over. | `MainActivity.kt:8760`, `:8777`, `:8877` |

The site now describes swiping and finding the moon phase in Location in both languages. The English Adhkar section explains the saved reading preference. The hero animation's alternate text names Fajr, Dhuhr, Asr, Maghrib and Isha in both languages. The static Dhuhr poster retains its own description. The Play listing can describe the same supported features, including the revised compass and widget artwork, while keeping language-specific details accurate. Background Adhan delivery, live compass readings, launcher-specific widget sizing and app restriction enforcement require device testing.

## Public privacy and native policy

The complete native policy dialog in `MainActivity.kt:7873` matches the preserved November 4 function in both languages. The public English text matches all four native English sections after removing markup, decoding entities and normalizing whitespace, line escapes and bullet markers. Its effective date matches January 1, 2024. Both public pages retain `prayerlockapp@gmail.com` as the contact.

The public Arabic page translates the full English policy. It has the same effective date with Western digits. All four Arabic public paragraphs differ in wording from the shorter native Arabic policy. The fuller public text retains the network geocoding explanation, interval windows and Android SharedPreferences. Both pages' policy text was retained for this export.

The source still declares `INTERNET` and uses Android Geocoder for city searches and coordinate labels (`AndroidManifest.xml:8`, `MainActivity.kt:4398`, `:4438`). This makes the English policy's network explanation material alongside its broad local-processing language. The manifest declares a narrow `MAIN`/`LAUNCHER` app-visibility query (`AndroidManifest.xml:15`). Backup is enabled (`AndroidManifest.xml:23`). Both backup XML files exclude `prayer_lock_prefs.xml` and include shared preferences generally. This leaves `adhkar_prefs`, including the new reading preference, eligible under the declared rules. The actual backup or transfer outcome depends on the device and system configuration.

The native privacy browser actions still open the website homepage (`MainActivity.kt:7996`, `:8132`). The dedicated public policy pages remain at `/privacy/` and `/ar/privacy/`. The manifest still lacks `SYSTEM_ALERT_WINDOW` and an Accessibility Service registration. `LockoutOverlayService.kt:491` still reports that the service is enabled and the default kickout-only path returns early at `:513`–`:526`. Website and listing copy use focus and reminder language. NFC remains in the source with its normal Settings control hidden (`MainActivity.kt:8579`).

This was a read-only review of the Android export. The website copy changes are limited to the two homepages. Capture, media, browser and deployment checks belong to the corresponding release evidence.
