# PrayerLock website

Build a quiet product page and a permanent `/privacy/` document for the Android app. The user's priorities are an Apple-like presentation, white space, screenshots, GIFs, motion, and free static hosting on GitHub Pages. All website work stays in `Website`; the Android project is unchanged.

## Design decisions

Use white #FFFFFF, mist #F5F6F8, ink #182238, muted slate #596477, sky #387AB4, and the app's gold #FFDF85. Use the bundled Plus Jakarta Sans family, supported by the platform sans-serif stack. Set oversized tightly spaced headlines against generous margins. The distinctive visual is the app's five prayer skies; give these the color and keep the surrounding site quiet. Use the real app logo. No stock photos, invented testimonials, counters, subscriptions, or unnecessary feature cards.

Page sequence: restrained navigation; centered “Make room for prayer.” hero with three app views; explanation of focus lockouts; interactive five-prayer sky gallery; Qibla/Adhkar/focus details; short local /brag product film; launch status and contact; privacy footer. Motion supports sky transitions and product demonstration. Provide a global pause control and reduced-motion support. Mobile layouts retain generous spacing with smaller type and one main phone view.

The static policy reproduces the in-app text and effective date, with the supplied support address prayerlockapp@gmail.com. It must load without JavaScript or login. Preserve wording; document source-audit discrepancies separately instead of silently rewriting the user's policy. No Google Play URL exists, so show an honest coming-soon state, not a dead download button.

## Implementation plan

- Create semantic `index.html`, shared `styles.css`, and progressive `app.js`; preserve navigation and privacy without JavaScript.
- Copy existing app artwork and font locally, record provenance, and replace or supplement with source-rendered Android screenshots if the build supports it.
- Produce /brag media in `brag-output`, copy optimized delivery media to `assets/media`, and embed with poster, captions, controls, and no automatic sound.
- Create `privacy/index.html`, `.nojekyll`, a GitHub Pages workflow, and setup instructions supporting repository subpaths.
- Verify all relative links/assets, policy text parity, keyboard controls, mobile/desktop overflow, media playback and reduced motion. Inspect rendered desktop/mobile screenshots and correct issues.

No runtime dependencies, analytics, third-party font requests, backend or database. This directory is not currently a Git repository; no commits or remote publication are part of this implementation.
