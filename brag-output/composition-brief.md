# Hyperframes Composition Brief: PrayerLock

Create an eighteen-second quiet premium product film, 1920×1080 at 30fps, using the full storyboard in brag-plan.md.

Output composition: `composition/`. Final render: `brag.mp4`. Website copies: `../assets/media/prayerlock-film.mp4`, `prayerlock-film-poster.jpg`, and `prayerlock-sky.gif`.

Source project: `C:/Dev/PrayerLock/App/prayerlock`. Read production MainActivity.kt/HomeTabScreen, LockoutOverlayService.kt, theme/Color.kt, theme/Type.kt, and drawable/ic_lock_logo_vector.xml. Logo paths are converted directly from the Android vector. Brand typography is the bundled Plus Jakarta Sans. Use local image assets and local GSAP runtime.

Copy: “Make room for prayer.”, “Give prayer your attention.”, “Scheduled distraction lockouts.”, “A little closer. Every day.”, “PrayerLock”, “For Android”, “Qibla”, “Adhkar”. The lockout scene uses the real rendered Maghrib OverlayContent screen. Make no claims about release availability or outcomes.

LOOK: #FBFBFD near-white stage; #1D1D1F ink; source #1B2646 sky and #FFDF85 accent; Plus Jakarta Sans 600/400; 84px headline; 32px supporting type; 220px content inset; 42px phone corners. BANNED: neon, bounce, fake metrics, stock people, ornamental particles, music, narration.

Audio role: intentional silence. No music, narration, SFX or reactive effects. Quiet is the concept and fits the prayer context and muted website autoplay. No cue analysis is required.

Implement four sub-compositions, using local, paused, seek-safe GSAP timelines. Carry the actual rendered production UI through deliberate device arrivals and the actual prayer-shield screen. Use registry fade-through timing guidance, adapted to the near-white stage. Run `hyperframes check`, inspect sampled frames, render locally, choose a settled product frame as poster, and bake that poster into only frame zero. Keep all original sources editable and do not publish.
