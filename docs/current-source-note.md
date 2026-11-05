# Source observation during the Qibla/Adhkar asset refresh

Historical review. Use [the November 5 alignment review](source-refresh-20261105.md) for app version 1.2 and policy parity.

The screenshot refresh uses the updated Android export and preserves the app files. It does not certify the app's runtime or release readiness. This note records a separate, concrete source finding rather than treating a UI capture as an enforcement test.

## Lockout implementation needs review

The current manifest registers no Accessibility Service and does not declare `SYSTEM_ALERT_WINDOW`. `MyAccessibilityService.kt` is a placeholder class. `MainActivity.kt` near lines 642–694 and 1495–1527 hard-codes the overlay/accessibility permission status to true instead of obtaining the previous grants.

`LockoutOverlayService.kt` near lines 482–517 returns early from the standard `showOverlay()` path when the default `is_kickout_only_mode` is true and `isAccessibilityServiceEnabled()` returns true. That check is now hard-coded. The remaining window code near lines 520–580 still attempts `TYPE_APPLICATION_OVERLAY`/`TYPE_PHONE`, whose permission is absent from this manifest. Allowed-app selections are saved, but the previous foreground-app observer has been removed.

These source paths do not substantiate the old marketing claim that the current release automatically blocks restricted apps or redirects them home. This is a source review, not a physical-device execution result. Review the intended enforcement implementation before publishing those claims. Screenshots of the remaining UI do not resolve the issue.

## Text drift

The app's native privacy dialog has new permission/geocoding and Local Storage text; the website and listing previously described the earlier Accessibility Service implementation. At the user's request, the website now reproduces that updated policy and promotional copy no longer claims active Accessibility Service enforcement. Exact policy synchronization still retains contradictions in the app's own text, including section 1's wholly local language versus section 2's network geocoding, and permission descriptions absent from the manifest. Copy synchronization is separate from resolving those source behaviors.
