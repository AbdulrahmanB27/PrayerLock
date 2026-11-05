# Arabic website and listing

Refreshed for app version 1.2 on November 5, 2026. English is at `/` and Modern Standard Arabic is at `/ar/`. Privacy documents are at `/privacy/` and `/ar/privacy/`. Relative links, shared CSS and JavaScript, and the GitHub Pages workflow support repository subpaths. Language switches use ordinary links.

Arabic pages translate existing copy, metadata, labels, image descriptions, prayer-sky announcements, and motion controls. `rtl.css` supplies Arabic typography and directional layout while preserving the English design. Tajawal regular is copied from the app; Bold and the bundled SIL Open Font License come from the Google Fonts Tajawal directory. All runtime requests remain local to the site.

The privacy page translates the existing policy, retaining its January 1, 2024 effective date and support email. Translation does not correct the implementation and policy inconsistencies documented in [privacy-review.md](privacy-review.md).

Current Arabic screenshots and GIFs come from the production Compose components with controlled sample data. Prayer names, times, counters, navigation, Qibla, Adhkar and many settings have native Arabic labels. Arabic Adhkar shows the Arabic text and repetition count. The public Arabic policy is the full translation of the English policy, including the Geocoder network caveat. Native rendering evidence is in `Website/tools/capture/refresh-20261105/` in the workspace.

The hero GIF loops through Dhuhr, Asr, Maghrib, Isha and Fajr. The separate selector lets visitors choose any of the five skies. The Adhkar GIF shows native counter and next-item states. The 22-second film uses version 1.2 English and Arabic app captures, with default Arabic captions on the Arabic page. Source and audio license details are in `Website/brag-output-2026-11-05/`.

The version 1.2 Arabic Google Play materials are in `PlayStore/localizations/ar/` and the combined upload archive.

The desktop language link now uses a small globe and a matching navigation treatment instead of a bordered pill; it sits last in the navigation order in both languages. The focus illustration uses the native transparent symbol in the existing dark variant for contrast on white.

The widget gallery shows three native English RemoteViews renders, with an English-example note on the Arabic page.
