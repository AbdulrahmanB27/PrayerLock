# PrayerLock website

A static product page and privacy policy for PrayerLock. No build, package installation, API, database, analytics, cookies, or paid service is required. All fonts, images and promotional media are hosted with the site.

## Preview locally

From this directory:

```powershell
python -m http.server 4173
```

Open `http://localhost:4173/`. The policy is at `http://localhost:4173/privacy/` and works with JavaScript disabled.

## Publish on GitHub Pages

For a clean upload, extract `release/prayerlock-pages.zip` and put its contents at the repository root. It contains the website, deployment workflow, licenses, and review notes, without the video-authoring tools or QA artifacts.

1. Create a public GitHub repository for the website. Put **the contents of `Website`** at that repository's root. Do not upload the Android app, signing keys or environment files.
2. Use `main` as the branch, or update `.github/workflows/pages.yml` to your branch name.
3. Open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Push the files. The included workflow copies only the public HTML, CSS, JavaScript, assets, and privacy page into the Pages artifact.
5. Open the successful deployment's URL. Your Play Console privacy URL will be `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/privacy/` (or `https://YOUR-USERNAME.github.io/privacy/` for a user site).

Every site link and asset path is relative, so repository subpaths work. GitHub Pages serves `privacy/index.html` as `/privacy/`; `/privacy` normally redirects to the trailing slash. Use the trailing-slash URL in Play Console.

If you keep this folder within a larger repository, GitHub only discovers workflows at that repository's root. Move `.github/workflows/pages.yml` to the root `.github/workflows/` and change the preparation step to copy from `Website/`. A dedicated website repository is the simplest setup.

GitHub's [official Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) describes Pages availability and deployment configuration. No deployment or GitHub repository was created by this task.

## Before the Google Play submission

The website preserves the app's existing four policy sections and **January 1, 2024** effective date, and adds the supplied public contact address. Read [the specific source-audit notes](docs/privacy-review.md) before submitting it: the current app policy's absolute local-only wording needs to be reconciled with Android Geocoder and backup settings. The notes are excluded from the Pages deployment. Hosting a policy does not establish Google Play approval.

After deployment, the Android app's `privacyUrl` can be set to the published URL in `MainActivity.kt`. That app source was not changed here.

## When the app launches

In `index.html`, replace the “Coming soon” link/status with the real Google Play listing, then update the film outro. No invented listing URL is used. Support links already use `prayerlockapp@gmail.com`.

## Files

- `index.html`, `styles.css`, `app.js`: the product page, responsive layout and progressive interactions.
- `privacy/index.html`: the independent policy document.
- `assets/`: self-hosted brand, font, eight source-rendered Android screens, two GIFs and the 18-second /brag film.
- `brag-output/`: editable /brag composition, storyboard, render and share copy. Excluded from deployment.
- `docs/`: design decisions, asset provenance and source-audit notes. Excluded from deployment.
- `output/playwright/`: local visual QA screenshots. Excluded from deployment.
- `release/prayerlock-pages.zip`: a compact, ready-to-upload repository snapshot.

Use `assets/fonts/OFL.txt` when redistributing the Plus Jakarta Sans font.
