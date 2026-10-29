# Brag Plan: PrayerLock

## Planning rubric
1. PrayerLock is an Android prayer companion with locally calculated prayer times, scheduled distraction lockouts, Qibla and Adhkar.
2. The strongest capability is the scheduled lockout at prayer time; no adoption, efficacy or launch-availability claims are made.
3. The visual hook is a calm, sky-coloured prayer dashboard floating on a near-white product stage.
4. Show the production Home screen, actual production prayer-shield UI, then production Qibla and Adhkar screens.
5. Eighteen seconds is sufficient; four scenes provide readable settled holds.
6. Preset: polished. Direction: quiet premium product film; generous space, precise type, no bounce.
7. Intentional silence: a website film for a prayer companion should make room for quiet. No music, SFX or narration; the website can autoplay muted without an audio surprise.
8. Share caption: PrayerLock for Android. Prayer times, distraction lockouts, Qibla and Adhkar—built around making room for prayer.
9. Flow: see the next prayer → prayer-time lockout appears → explore Qibla and Adhkar. Screens are actual production Compose components rendered in a JVM capture harness, not a device recording or live interaction.

## The angle
Make room for prayer. The product, including its real changing-sky design and calm lockout, does the visual work. Supporting language remains a frame around the real feature flow.

## Format and duration
Landscape, 1920 × 1080, 30 fps, 18.0 seconds.

## Visual identity
Source: `app/src/main/java/com/example/ui/theme/Color.kt`, `Type.kt`, `MainActivity.kt`, `LockoutOverlayService.kt`, and the app logo vector.
Stage #FBFBFD; text #1D1D1F; source sky #1B2646; source accent #FFDF85; source secondary #AEC0DF. Plus Jakarta Sans from the app, with source logo paths preserved.
LOOK: near-white #FBFBFD stage; source sky-blue app surfaces; Plus Jakarta Sans 600/400; title 84px, body 32px; 220px safe inset; 42px phone corner; subtle 18% shadow. BANNED: neon, bounce, fake metrics, stock people, ornamental particles, music, narration.

## Storyboard

### 1. Room — 0.0–4.8s (4.8s)
Source Home screen appears at right. Left: PrayerLock identity and “Make room for prayer.” The device settles during the first second; text holds for more than three seconds. Real app screen content is the hook.
Sequential interaction: wordmark first, headline next, phone entrance overlapping naturally.
Transition: source phone carries into a new composition with the same near-white stage.
Audio: intentional silence.

### 2. Attention — 4.8–10.4s (5.6s)
Home screen at left; right reads “Give prayer your attention.” Supporting line: “Scheduled distraction lockouts.” The actual Maghrib prayer-shield component enters over the Home screen, with its “PRAYER SHIELD ACTIVE” and focus timer. The film never simulates completion or falsely implies a recorded tap.
Sequential interaction: dashboard → lockout card → settled hold of 2.5 seconds.
Transition: outgoing phone eases left and next pair arrives.
Audio: intentional silence.

### 3. Direction and remembrance — 10.4–14.8s (4.4s)
Production Qibla and Adhkar screens side by side. Left: “A little closer. Every day.” The two short feature names sit with the phones. Staggered arrivals are 0.25s apart, followed by a 3s readable hold.
Sequential interaction: Qibla arrives, then Adhkar; no fabricated compass interaction or spiritual outcomes.
Transition: calm fade-through, registry recipe adapted to the same white ground.
Audio: intentional silence.

### 4. Identity — 14.8–18.0s (3.2s)
Exact app logo above PrayerLock. “Make room for prayer.” and “For Android.” The final lockup settles by 15.6s and holds through the end. No “download now” claim because no Play listing was supplied.
Sequential interaction: logo and name, then tagline.
Audio: intentional silence.

## Media provenance
Final assets use only real production Compose renders from `Website/assets/screenshots`. These are JVM-rendered production UI, distinct from on-device captures. No initial concept-art fallback is included in the final film or GIF. All sample locations/times are demonstration data. No private user data is shown.

## Delivery
Local Hyperframes composition plus MP4, deliberate JPEG poster baked as frame zero, optimized short GIF loop, composition brief, share copy and provenance notes. No publishing.
