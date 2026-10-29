# PrayerLock media notes

The film and sky loop use **actual production Android Compose UI rendered by a JVM screenshot harness**. They are not emulator captures, physical-device screenshots, live app recordings, or artist recreations. The visual-assets task captured unmodified HomeTabScreen, QiblaTabScreen, AdhkarTabScreen and OverlayContent with sample data at 780×1688. The Home location, schedule and countdown are demonstration values. Qibla is rendered with sample/simulated sensor state, not a live location measurement.

Screens used: `Website/assets/screenshots/home-isha.png`, `home-maghrib.png`, `prayer-shield.png`, `qibla.png`, `adhkar.png`. The GIF uses all five Home sky-state PNGs. No supplied AI Studio concept art is used in final media. Editing motion adds generic Android phone frames and controlled screen transitions; it does not fabricate recorded taps or a completed prayer.

The logo SVG preserves exact paths and fill colours from the app's `res/drawable/ic_lock_logo_vector.xml`, on a source-colour navy square. Display typography uses the official Plus Jakarta Sans variable font and the site's OFL license. Local GSAP 3.15.0 is included, so rendering does not rely on a CDN.

The film is intentionally silent: no music, sound effects, or narration. Silence is the deliberate creative choice for a calm prayer companion and muted website playback. The Hyperframes `film_silent` warning is therefore expected. There are no paid media calls or generated voices.

The 18s landscape film is locally rendered by Hyperframes 0.8.217. Its settled hero at 2.4s is selected as the JPEG poster and baked into frame zero of the final MP4. Exact scene timings and text descriptions are supplied in `Website/assets/media/prayerlock-film.vtt`.

The website GIF is 390×844, 6.60s, 25 frames, infinitely looping. It uses a shared 192-colour palette without dithering to avoid shimmer; 1.00s hold plus four 80ms transition frames per sky state.

Current Hyperframes skill contract was read from upstream commit `4e2a1c215a42c6d262b8c635df9d5edff80e8830` (hyperframes, hyperframes-cli, hyperframes-registry and media-use). Registry `fade-through` was searched, installed, and its restrained timing recipe adapted. No assets or site were published.

Regeneration: run `python build_composition.py`, then `npx --yes hyperframes@0.8.217 check` inside `composition`, inspect sampled frames, and render with `npx --yes hyperframes@0.8.217 render --quality delivery --output ../brag.raw.mp4`. Then run `python finalize_media.py` and `python make_sky_loop.py` from this folder. Check final dimensions, duration and thumbnails before release.
