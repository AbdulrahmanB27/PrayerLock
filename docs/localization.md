# Arabic website and listing

Refreshed for app version 1.1 on November 4, 2026. English stays at `/`; Modern Standard Arabic is at `/ar/`. Privacy documents are at `/privacy/` and `/ar/privacy/`. Relative links, shared CSS/JS, and the GitHub Pages workflow support repository subpaths without a build or backend. Language switches use ordinary links; there is no locale cookie or automatic redirect.

Arabic pages translate existing copy, metadata, labels, image descriptions, prayer-sky announcements, and motion controls. `rtl.css` supplies Arabic typography and directional layout while preserving the English design. Tajawal regular is copied from the app; Bold and the bundled SIL Open Font License come from the Google Fonts Tajawal directory. All runtime requests remain local to the site.

The privacy page translates the existing policy, retaining its January 1, 2024 effective date and support email. Translation does not correct the implementation and policy inconsistencies documented in [privacy-review.md](privacy-review.md).

Current Arabic screenshots and GIFs come from the updated production Compose components with controlled sample data. Prayer names, times, counters, navigation, Qibla, Adhkar and many settings now have native Arabic labels. Arabic Adhkar intentionally hides English translation and transliteration, and the website copy/alt text reflects that. The latest app also adds Arabic onboarding and a shorter native Arabic policy. The public Arabic policy remains the fuller translation of the unchanged English policy, including the Geocoder network caveat. The site does not claim every system dialog is translated. Native rendering evidence for this refresh is in `Website/tools/capture/refresh-20261104/` in the workspace. The earlier morning snapshots are historical.

The current hero GIF holds three brighter native screens (Dhuhr, Asr and Fajr); the separate selector still offers all five prayer skies. The Adhkar GIF holds native counter/next-item states. Neither is a physical-device screen recording. The new 22-second film includes native English and Arabic examples, English editorial text, and default Arabic captions on the Arabic page. Source, reproduction and audio-license evidence are in the current timestamped `/brag` output directory. The original `build_arabic_media.py` and earlier media reports describe the prior run.

Arabic Play Store materials from the earlier listing task remain in `PlayStore/localizations/ar/`. This website refresh does not update or submit that separate pack. The current task publishes the static website through the existing GitHub Pages repository.

The desktop language link now uses a small globe and a matching navigation treatment instead of a bordered pill; it sits last in the navigation order in both languages. The focus illustration uses the native transparent symbol in the existing dark variant for contrast on white.

The three new widget examples are actual English RemoteViews renders, including on the Arabic page with an explicit English-example note. The native Arabic widget host previews did not render reliably and were excluded; this is a renderer limitation, not a verified device defect. Native Arabic phone screenshots and captions remain available throughout.
