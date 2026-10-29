# Specific policy review notes

The public policy is copied from `App/prayerlock/app/src/main/java/com/example/MainActivity.kt`, `NativePrivacyPolicyDialog` (lines 7518–7605 in the supplied source), with the supplied contact `prayerlockapp@gmail.com` added. Its effective date remains January 1, 2024. The Android app has not been modified.

The following are source findings to resolve before relying on this text for a Play submission:

1. The policy says all geographical adjustments happen entirely locally and location is never shared. The app calls Android `Geocoder.getFromLocation()` with coordinates in `MainActivity.kt` near lines 1335–1336. Check how the target devices' geocoding service handles those coordinates and describe the behavior accurately.
2. The manifest sets `android:allowBackup="true"`, with default cloud-backup rules and no exclusions in `res/xml/data_extraction_rules.xml` and `backup_rules.xml`. Check what Android backs up before claiming all preferences remain solely on the phone.
3. The app handles installed-app selection, local prayer logs and optional NFC identifiers; these are not explained in the existing four sections. Check whether the policy should describe their handling, retention and deletion. Verify the final packaged build and all included SDKs as well.
4. The existing accessibility configuration disables retrieving window content and performing gestures, which supports part of the policy's description. Continue to ensure the prominent disclosure and Play Console declarations match actual behavior.

Google's current [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) calls for an accurate privacy policy on a publicly accessible URL, developer/contact information, and descriptions of data handling. The policy is not a PDF, requires no login, and renders without JavaScript. Those properties do not resolve the content discrepancies above. This document records implementation findings; it is not a legal compliance determination.

No analytics, ads, account flow, active Gemini calls or direct HTTP requests were found in the Kotlin source during this website task. Network libraries and INTERNET permission remain present, so the site avoids adding stronger privacy marketing claims.
