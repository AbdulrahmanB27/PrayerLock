# Current screenshot refresh — November 4, 2026

All visible phone screenshots use the latest native export, favouring genuine Dhuhr/Asr daytime colors. Main features now use brighter native Qibla, Adhkar and Dhuhr focus views; the hero uses Fajr, Dhuhr and Asr. Five original prayer moments remain in the interactive selector. The widget gallery uses three actual English native widget renders, explicitly labelled English on the Arabic page. No image was recolored and no separate light theme is claimed.

Usable capture provenance: `Website/tools/capture/refresh-20261104/README.md` and `capture-manifest.json` in the local workspace. Public-path hashes and the source selection are in `Website/output/nov4-screenshot-integration.json`. Earlier records below are historical.

# Current screenshot refresh — November 3, 2026

All visible website screenshots and both language GIF sets now use the version 1.1 export. There are 36 native 780 × 1688 captures and 28 passed native tests. Production main-source hashes match all 81 current files. The public timetable options image uses a genuine scrolled seven-row state, including optional Sunrise and Last Third. Harness, sample settings, hashes and limitations are in `Website/tools/capture/refresh-20261103/` in the local workspace. Public-path integration hashes are in `Website/output/current-screenshot-integration.json`. Earlier provenance below is historical.

# PrayerLock UI capture provenance

The website uses a mixture of retained October 29 captures and refreshed October 31 Qibla/Adhkar captures. All are genuine Android Compose source renders. They are not AI Studio design concepts, browser recreations, physical-device photographs, or live device recordings.

## Asset origins

All website PNGs in `assets/screenshots/` are 780 × 1688 pixels, rendered natively at 390 × 844 dp and xhdpi. Operating-system bars are omitted; none were fabricated.

| Files | Capture origin |
| --- | --- |
| `home-fajr.png`, `home-dhuhr.png`, `home-asr.png`, `home-maghrib.png`, `home-isha.png`, `prayer-shield.png` | October 29 source snapshot; retained byte-for-byte during the UI refresh |
| `qibla.png`, `adhkar.png` | Updated app source captured October 31, about 23:18 UTC |
| `adhkar-step-00.png` through `adhkar-step-04.png` | Updated Adhkar source and real UI interactions, captured October 31 |

The initial screenshot batch passed 8 tests, with 0 failures and 0 errors. Its historical harness and XML result remain in `tools/capture/`. The older interaction-only result there records 1 passing test; it does not describe the replacement five-frame sequence.

The refresh used an isolated copy of the current `App/prayerlock` source, Robolectric API 35 native graphics, Roborazzi 1.59.0, Gradle 9.5.0, and Android Studio JBR. It called the production `QiblaCompassScreen`, `AdhkarTabScreen`, and `CustomBottomNavigation` composables with the dashboard's gradient/scaffold structure. No production app files were edited, and no emulator or SDK was installed.

## Demonstration data

The retained Home captures use the original fixture: Lower Swatara Township; Fajr 5:55 am, sunrise 7:25 am, Dhuhr 12:39 pm, Asr 3:45 pm, Maghrib 6:17 pm, and Isha 7:32 pm. These are demonstration values, not a live prayer timetable. Their moon and Hijri date reflect the original capture date.

The refreshed Qibla fixture uses public New York coordinates 40.7128, -74.0060 and a simulated north-facing phone heading. It is not a sensor-accuracy or physical calibration test. The refreshed Adhkar view uses the production Maghrib list, now 15 items, and its default Arabic font preference. No account or personal data is included.

## Refreshed Adhkar interaction states

| Frame | Actual rendered state |
| --- | --- |
| `adhkar-step-00.png` | First remembrance, counter 0 of 3 |
| `adhkar-step-01.png` | Counter 1 of 3 after the production click handler |
| `adhkar-step-02.png` | Counter 2 of 3 after the second click |
| `adhkar-step-03.png` | Completed checkmark about 116 ms after the third click; the progress ring is still animating |
| `adhkar-step-04.png` | Second remembrance, page 2 of 15, counter 0 of 1 |

The production code schedules automatic page advancement after 350 ms. Native test-clock settlement of that animation stalled in the harness, so frame 04 was reached using the production pager's accessibility scroll-to-index action. The next-page and reset-counter semantics were asserted. These are real UI states assembled into a demonstration, not a real-time recording of automatic advancement. Keep the completed frame brief when encoding media; the agreed hold is 0.3 seconds before the next remembrance.

The GIF at `assets/media/prayerlock-adhkar.gif` and film are derived media assembled from these states. Their encoding output is maintained by the media workflow; the earlier four-frame GIF's size and completion-only description are historical, not specifications of the refreshed media.

Suggested caption: "Count each remembrance, one tap at a time."

Suggested alternative text: "PrayerLock's Adhkar counter advances to completion, then shows the next remembrance."

## Evidence and verification

The fresh capture harness, source hashes, source delta, four XML results, and published PNG manifest are retained in [the October 31 refresh snapshot](../../PlayStore/source/capture/refresh-20261031-1907/README.md). The refresh passed 10 tests: 3 website, 3 phone, and 2 for each tablet viewport; 0 failures and 0 errors.

On November 1, a read-only verification confirmed that all 80 current production source/resource files still match that snapshot, all 14 published website/Play Store refresh images match their hashes and expected RGB24 dimensions, and all 16 unaffected Home/shield PNGs remain byte-identical. No images were recaptured during this verification. The retained October 29/earlier October 31 stills are not presented as newly captured from the updated source.
