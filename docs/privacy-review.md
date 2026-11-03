# Specific policy review notes

Historical review: the November 3 app export is now covered by [the current alignment review](source-refresh-20261103.md). Use that report for present behavior, manifest changes and policy parity.

The public policy was synchronized again on October 31, 2026 from `App/prayerlock/app/src/main/java/com/example/MainActivity.kt`, `NativePrivacyPolicyDialog` (near lines 7509–7596 in this export), with the supplied contact `prayerlockapp@gmail.com` retained. Its effective date remains January 1, 2024, as written in the app. The Android app has not been modified by this refresh.

The following are source findings to resolve before relying on this text for a Play submission:

1. Section 1 still says geographical adjustments happen entirely locally. Section 2 now explicitly states that Android Geocoder may query network providers when searching cities or resolving coordinate labels. The source uses those Geocoder paths. Exact synchronization preserves both statements; their inconsistency still needs review.
2. The manifest still enables Android backup. The updated backup/extraction XML excludes `prayer_lock_prefs.xml` while including other shared preferences. Check all actual preference files, including `adhkar_prefs`, before describing which data may be backed up or transferred.
3. Section 2 now describes Draw Over Other Apps and an app-visibility `<queries>` block, but this export's manifest declares neither `SYSTEM_ALERT_WINDOW` nor `<queries>`. Accessibility Service was removed; its old privacy/listing references have been removed from the synchronized text. Check permission descriptions against the final packaged manifest.
4. The source still handles local schedules, prayer logs and optional NFC identifiers. Check whether retention/deletion and the full SDK behavior are adequately described. No new legal promises were authored during this asset update.

Google's current [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) calls for an accurate privacy policy on a publicly accessible URL, developer/contact information, and descriptions of data handling. The policy is not a PDF, requires no login, and renders without JavaScript. Those properties do not resolve the content discrepancies above. This document records implementation findings; it is not a legal compliance determination.

The refreshed marketing copy does not claim active Accessibility Service monitoring, home-screen redirection or guaranteed app blocking. A separate source review found a default lockout early-return path and missing overlay permission plumbing; details are recorded in [the source observation](current-source-note.md). That behavior was not fixed or validated on a physical device by this screenshot task.
