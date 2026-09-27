# Chico's Oven

Chico's Oven is a modern bakery-themed Flask website designed to showcase a local bakery brand, highlight menu offerings, and present a polished online presence for customers. The project includes a responsive storefront layout, landing pages for key business sections, and a static export workflow for publishing to GitHub Pages.

## Project overview

This project was built as a small but complete web experience for a bakery business. It includes:

- A visually rich landing page with a hero section and brand messaging
- Menu and donut-specific content pages
- About, contact, gallery, privacy, and legal pages
- Fixed navigation and scrolling effects for a premium storefront feel
- Flask route-based page generation for clean, maintainable site structure
- Static export support for GitHub Pages publishing

## Tech stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- GitHub Pages-compatible static export

## Repository structure

- `bakery/app.py` — Flask application and route definitions
- `bakery/templates/` — page templates for the site
- `bakery/static/` — CSS, JavaScript, and image assets
- `build_preview.py` — renders the Flask pages into the `docs/` folder for static hosting
- `docs/` — generated GitHub Pages output

## Local installation

From the repository root in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r bakery/requirements.txt
```

If your environment already has a virtual environment set up, you can skip the setup step and run the app directly.

## Running the app locally

Start the Flask development server:

```powershell
.\.venv\Scripts\python.exe bakery/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

> Do not open the template files directly in the browser. They must be served through Flask so the CSS, images, and route links resolve correctly.

## Using the site

The app currently includes pages for:

- Home
- Menu
- Donuts
- Custom Donuts Gallery
- About Us
- Contact Us
- Privacy Policy
- Terms and Conditions

Navigation and page links are generated through Flask routes, which keeps the site organized and easier to maintain.

## GitHub Pages preview export

To generate the static GitHub Pages version of the site from the Flask app:

```powershell
.\.venv\Scripts\python.exe build_preview.py
```

This script:

- loads the Flask app,
- renders each page as HTML,
- writes the output into the `docs/` directory,
- copies static assets into `docs/static/`,
- creates a `.nojekyll` file for GitHub Pages compatibility.

Once generated, the static site can be published from the `docs/` folder using GitHub Pages settings in the repository.

## Notes

- Place images in the relevant `bakery/static/images/` folders to populate the hero and other sections.
- The project is intended for local development and static preview generation, not as a production deployment server.
- The GitHub Pages export is meant to provide a static snapshot of the site, while the Flask app remains the main development environment.

## About the commit count

The local repository history here shows a small number of commits for the current branch, and the generated GitHub Pages files are still in an uncommitted state. That means the extra commit count you are seeing is not explained by the new `docs/` pages alone in this workspace. It may be due to:

- earlier work on a different branch or remote history,
- repeated force-pushes or branch merges,
- a different repository state than the one currently checked out locally.

If you want, I can also help you clean up the Git history or explain the exact GitHub Pages publishing setup for this site.

