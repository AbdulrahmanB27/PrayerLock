# PrayerLock v1.3 website copy and privacy alignment

Reviewed the November 5, 2026 23:41 Android export on November 6. The configured app is PrayerLock `1.3`, version code `4`, package `com.prayerlockapp`, minimum SDK 24 and target SDK 36. The 95 configured production files match `App/prayerlock.zip` byte for byte. The ZIP SHA-256 is `93383b1e531cb12f1ed68ee96dcf2ab476f27896cd9535682e4bb02edaf0eb9c`.

## Product copy

- The English and Arabic homepages mention language and reminder preferences in setup and the optional Home guide to Settings, prayer times and Quick Actions. The new guide is a four-page setup with a separate optional coach-mark tour. It appears after the initial disclosure and permission screen. The website describes the controls and guide without implying that language or location selection precedes that gate. Source `OnboardingTourDialog.kt:184–224,299–331,595–720` and `MainActivity.kt:752–806,3591–3705`.
- Home location supports city search, device location and manual coordinates. The local calculation method, time offsets, Adhan voice and lunar-phase action are present. Source `MainActivity.kt:4483–4855,5400–5460,8940–9460`. The product page retains the lunar-phase sentence. The earlier preference to omit it applied to the Play listing.
- Focus language describes configuring a session inside PrayerLock. The supplied manifest has no overlay permission or Accessibility Service, and the default service path adds no window. The pre-Adhan reminder text distinguishes configured lead time from Android delivery. Source `AndroidManifest.xml:5–20,42–45`, `LockoutOverlayService.kt:507–543` and `MainActivity.kt:9313–9385,12708,12948`. [Android alarm scheduling](https://developer.android.com/develop/background-work/services/alarms)
- Both pages keep the canonical listing URL and the closed-test language for invited testers. Store-track status was supplied by the owner. A previous signed-out check of that URL returned 404. This source review does not establish what an enrolled account sees. [Google Play closed testing](https://support.google.com/googleplay/android-developer/answer/9845334?hl=en)

## Public privacy text

The four substantive sections, headings and January 1, 2024 date in the native dialog match the noon November 5 and 21:16 exports. The v1.3 browser actions link to the dedicated English and Arabic policy routes. The prior public English page matched all four native sections. The public Arabic page used a fuller translation of English, with a Geocoder disclosure absent from native Arabic. Source `MainActivity.kt:8133–8273,8401,10783–10792`.

The revised public pages use parallel English and Arabic wording based on the current implementation. Both retain January 1, 2024 and `prayerlockapp@gmail.com`. This intentionally replaces exact English native/public body parity and the earlier Arabic translation of the unchanged native English policy. The native dialog still has its original wording and remains a follow-up for the app owner.

| Public statement | Evidence |
| --- | --- |
| Prayer time and Qibla calculations run on-device, while Android Geocoder may use a network provider for a city search or a coordinate lookup. | `MainActivity.kt:1392,4566,4606,6541,6614,12551–12574,15071`. The exact system provider and request handling vary by device. [Android Geocoder](https://developer.android.com/reference/android/location/Geocoder) |
| Optional settings can list launchable apps and store selected packages locally. | The manifest has a targeted `MAIN`/`LAUNCHER` query at `AndroidManifest.xml:15–20`. `MainActivity.kt:1520–1524,14081–14092` stores selections and queries the launcher. `TahseenManager.kt:127–131` stores selected packages. |
| Notifications, Adhan audio and optional Masjid ringer changes use Android facilities. Custom audio uses access to the file the user selects. | `MainActivity.kt:2087–2108,12979–13317` and `MasjidVibrateManager.kt:12–68`. The public copy removes the older exact-timing and Draw Over Other Apps claims. |
| Linked NFC tags use their identifiers, and copying a Hadith citation writes it to the system clipboard. | `MainActivity.kt:633–648,1482–1487,11768–11781`. `AdhkarTab.kt:427–435`. Neither statement asserts NFC identity assurance. |
| Preferences persist across sessions. The declared Android backup rules exclude the main PrayerLock and Adhkar preference files. | `AndroidManifest.xml:22–25`, `res/xml/backup_rules.xml:8–12` and `res/xml/data_extraction_rules.xml:7–17`. Android backup remains enabled for eligible data. Both policies explain local data removal through Android's app storage settings. [Android Auto Backup](https://developer.android.com/identity/data/autobackup) |

## Remaining verification

- Bring the native permission disclosure and offline policy fallback into line with the public text. The first-run disclosure still describes Draw Over Other Apps and the native policy still says exact reminders. The source review also found app scheduling before setup, permission recovery gaps, and in-app focus state without demonstrated cross-app enforcement. [v1.3 source audit](../../Audit/2026-11-05-v1.3/security-privacy.md)
- The owner should verify the signed AAB's merged manifest and dependency set, the geocoding paths on supported devices, the effective backup behavior, and the developer identity and disclosures entered in Play Console. This review does not certify those declarations or the store track. [Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), [Play Data safety form](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)
