# Chico's Oven

## Website preview for class

**[Open the Chico's Oven website](https://MaxP2027.github.io/chicos-oven/)**

This public preview runs on GitHub Pages without Python or VS Code. It displays the Flask-rendered pages, logo, styling, and navigation. Ordering links are placeholders until store URLs are supplied; no backend runs on GitHub Pages.

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
python.exe -m pip install -r requirements.txt


**This is a local preview, not a public website.** The link only works on the computer running Flask, while the server is running. Putting this link on GitHub does not host the app. If you see "connection refused," start Flask using one of the methods above.

Do not open HTML templates directly. Flask must render them to load the styling, images, and page content.


See [bakery/README.md](bakery/README.md) for the structure and image filenames.
