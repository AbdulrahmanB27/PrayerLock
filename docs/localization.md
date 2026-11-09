# Arabic website and listing

Refreshed for app version 1.9 on November 9, 2026. English is at `/` and Modern Standard Arabic is at `/ar/`. Privacy documents are at `/privacy/` and `/ar/privacy/`. Relative links, shared CSS and JavaScript, and the GitHub Pages workflow support repository subpaths. Language switches use ordinary links.

Arabic pages translate existing copy, metadata, labels, image descriptions, prayer-sky announcements, and motion controls. `rtl.css` supplies Arabic typography and directional layout while preserving the English design. Tajawal regular is copied from the app; Bold and the bundled SIL Open Font License come from the Google Fonts Tajawal directory. All runtime requests remain local to the site.

The Arabic privacy page translates the public English policy, retaining its January 1, 2024 effective date and support email. The [November 9 source review](source-refresh-20261109.md) records differences from the embedded app text.

Current Arabic screenshots and GIFs come from the production Compose components with controlled sample data. Prayer names, times, counters, navigation, Qibla, Adhkar and many settings have native Arabic labels. Arabic Adhkar shows the Arabic text and repetition count. The public Arabic policy is the full translation of the English policy, including the Geocoder network caveat. Native rendering evidence is in `Website/tools/capture/refresh-20261109/` in the workspace.

The hero GIF loops through Dhuhr, Asr, Maghrib, Isha and Fajr. The separate selector lets visitors choose any of the five skies. The Adhkar GIF shows native counter and next-item states. The 22-second film uses English and Arabic renders of the current app screens, with default Arabic captions on the Arabic page. Source and audio license details are in `Website/brag-output-2026-11-09/`.

The Arabic Google Play materials, including the version 1.9 feature graphic and phone and tablet captures, are in `PlayStore/localizations/ar/` and the combined upload archive.

The desktop language link now uses a small globe and a matching navigation treatment instead of a bordered pill; it sits last in the navigation order in both languages. The focus illustration uses the native transparent symbol in the existing dark variant for contrast on white.

The widget gallery shows three native English RemoteViews renders, with an English-example note on the Arabic page.
