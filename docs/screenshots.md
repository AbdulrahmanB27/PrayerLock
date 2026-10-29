# PrayerLock UI captures

These PNGs are actual Android Compose renders of the app source in `App/prayerlock`, captured on 2026-10-29. They are not the pre-existing AI Studio design concepts, browser recreations, or photographs of a physical device.

The production Kotlin UI files were copied without changes to a temporary build at `C:/Users/abody/AppData/Local/Temp/PrayerLock-capture-20261029`. A test-only harness rendered the production composables using Robolectric API 35 native graphics and Roborazzi 1.59.0. No changes were made to the app checkout and no emulator was installed or launched.

All eight captures are 780 × 1688 pixels at a 390 × 844 dp viewport. They omit operating-system status and navigation bars. Home uses the actual `HomeTabScreen` and `CustomBottomNavigation` composables inside the same gradient/scaffold structure used by the app dashboard. Qibla and Adhkar use the actual `QiblaCompassScreen` and `AdhkarTabScreen`. The prayer shield uses the actual `OverlayContent` composable.

Sample prayer times and location were supplied by the harness: Lower Swatara Township, Fajr 5:55 am, sunrise 7:25 am, Dhuhr 12:39 pm, Asr 3:45 pm, Maghrib 6:17 pm, Isha 7:32 pm. These are demonstration values, not a live prayer timetable. Qibla uses sample coordinates 40.1965, -76.7436 with a simulated phone heading of north. Moon and Hijri-date rendering use the capture date. Each Home sky state is explicitly selected to demonstrate its corresponding theme. The prayer-shield countdown shows its initial state.

Files:

- `home-fajr.png`, `home-dhuhr.png`, `home-asr.png`, `home-maghrib.png`, `home-isha.png`
- `qibla.png`, `adhkar.png`, `prayer-shield.png`

The harness and passing XML result are in `Website/tools/capture/`. The initial screenshot batch passed: 8 tests, 0 failures, 0 errors. A valid Android SDK and Gradle are required to reproduce; the original app export does not include a Gradle wrapper.

## Adhkar interaction GIF

`Website/assets/media/prayerlock-adhkar.gif` shows actual Adhkar composable states captured after its production click handler increments the first remembrance counter: 0, 1, 2, and the completed checkmark with the full progress ring. The capture stops at completion; it does not show progression to the next remembrance. Four original 780 × 1688 PNG frames are retained as `adhkar-step-00.png` through `adhkar-step-03.png`. `prayerlock-adhkar.png` is the static first-frame fallback.

FFmpeg encoded the four source frames as a looping 520 × 1125 GIF, 6.2 seconds long, 156,958 bytes. The frame list and hold times are in `Website/tools/capture/adhkar-frames.txt`. The output was probed for dimensions/duration and fully decoded with FFmpeg without errors. This is an interaction demonstration assembled from real Android-rendered states, not a physical-device screen recording. It contains no account or personal data.

The final interaction-only test passed: 1 test, 0 failures, 0 errors. Evidence is retained in `Website/tools/capture/interaction-results.xml`.

Suggested visible caption: "Count each remembrance, one tap at a time."

Suggested alternative text: "PrayerLock Adhkar counter advances from zero through two, then shows completion."

Capture command from the temporary project, with Android Studio JBR as `JAVA_HOME` and the installed SDK as `ANDROID_HOME`:

```powershell
gradle ':app:testDebugUnitTest' '--tests' 'com.example.MarketingCaptureTest' '-Proborazzi.test.record=true' '--console=plain'
```

Production source SHA-256:

```text
MainActivity.kt        A18E018765F2C25FB1F77B45697350004E70A6B65D93D6D4063E75E62DFB7AC2
AdhkarTab.kt           9F031D2E3F7CE0B3CD3CE43A25B1869050E8141279AF07B99168F1997C9D764D
LockoutOverlayService.kt FB02293C4E69A25427C639424EE4A561A2DC7EC07CADD870CC006F7EF954AB5C
```
