# PrayerLock website

A static product page and privacy policy for PrayerLock. No build, package installation, API, database, analytics, cookies, or paid service is required. All fonts, images and promotional media are hosted with the site.

Production: [English](https://abdulrahmanb27.github.io/PrayerLock/) · [Arabic](https://abdulrahmanb27.github.io/PrayerLock/ar/) · [Privacy policy](https://abdulrahmanb27.github.io/PrayerLock/privacy/) · [Arabic policy](https://abdulrahmanb27.github.io/PrayerLock/ar/privacy/). Repository: [AbdulrahmanB27/PrayerLock](https://github.com/AbdulrahmanB27/PrayerLock).

The November 5 refresh follows app version 1.2. The hero loops through all five prayer skies, starting at Dhuhr, and the rest of the page favors native daytime imagery. The Qibla compass, Adhkar controls, widgets and 22-second film use the current app screens. Source evidence is in [the current alignment review](docs/source-refresh-20261105.md).

## Preview locally

From this directory:

```powershell
python -m http.server 4173
```

Open `http://localhost:4173/`. The policy is at `http://localhost:4173/privacy/` and works with JavaScript disabled.

The Arabic site is at `http://localhost:4173/ar/`, with its privacy translation at `/ar/privacy/`. Language links switch between matching English and Arabic pages. Both languages use static HTML and relative paths. Arabic uses self-hosted Tajawal, right-to-left layout, translated controls, native Arabic-mode screenshots and GIFs, and Arabic captions for the existing English film. Phone screens use the native Arabic UI; widget examples on the Arabic page are labelled English. See [localization notes](docs/localization.md).

## Publish on GitHub Pages

For a clean upload, extract `release/prayerlock-pages.zip` and put its contents at the repository root. It contains the website, deployment workflow, licenses, and review notes, without the video-authoring tools or QA artifacts.

1. Use the existing `AbdulrahmanB27/PrayerLock` website repository. Put the packaged static site at its root, preserving repository-specific files. The app source, signing files and environment files are outside the website package.
2. Use `main` as the branch, or update `.github/workflows/pages.yml` to your branch name.
3. Open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Push the files. The included workflow copies only the public HTML, CSS, JavaScript, assets, and privacy page into the Pages artifact.
5. Open the successful deployment's URL. The Play Console privacy URL is `https://abdulrahmanb27.github.io/PrayerLock/privacy/`.

Internal links and asset paths are relative so repository subpaths work. GitHub Pages serves `privacy/index.html` as `/privacy/` and normally redirects `/privacy` to the trailing-slash URL. Use the trailing-slash URL in Play Console.

If you keep this folder within a larger repository, GitHub only discovers workflows at that repository's root. Move `.github/workflows/pages.yml` to the root `.github/workflows/` and change the preparation step to copy from `Website/`. A dedicated website repository is the simplest setup.

GitHub's [official Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) describes the deployment configuration. The existing repository is configured to build Pages using GitHub Actions.

## Before the Google Play submission

The English policy reproduces the native policy, including its Permissions and Local Storage sections, **January 1, 2024** effective date, and supplied contact address. The public Arabic policy is a full translation of the English policy. [The current source review](docs/source-refresh-20261105.md) records policy and implementation details. The deployment workflow serves the policy pages and excludes the review notes.

The app's current `privacyUrl` opens the homepage; the dedicated policy route is `/PrayerLock/privacy/`. The website refresh does not modify Android source.

## Google Play link

Both homepages link to the [PrayerLock Google Play listing](https://play.google.com/store/apps/details?id=com.prayerlockapp) and identify the current closed test for invited testers. When the production release is available, update the availability copy in both languages and retain the same listing URL. The support address is `prayerlockapp@gmail.com`.

## Files

- `index.html`, `styles.css`, `app.js`: the product page, responsive layout and progressive interactions.
- `privacy/index.html`: the independent policy document.
- `assets/`: self-hosted brand/fonts, current native Android screens in both languages, four GIFs and the 22-second /brag film with captions.
- `brag-output-2026-11-04-152322/`: current editable /brag composition, storyboard, render, credits and share copy in the local workspace. Excluded from deployment.
- `docs/`: design decisions, asset provenance and source-audit notes. Excluded from deployment.
- `output/playwright/`: local visual QA screenshots. Excluded from deployment.
- `release/prayerlock-pages.zip`: a compact, ready-to-upload repository snapshot.

Use `assets/fonts/OFL.txt` when redistributing the Plus Jakarta Sans font.
Tajawal's license is included as `assets/fonts/Tajawal-OFL.txt`.
Film audio credits and license links are in `assets/media/credits.txt` and below the player. Playback starts only after a visitor selects play.
