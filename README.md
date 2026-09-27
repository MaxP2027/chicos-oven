# Chico's Oven

Flask bakery website first draft.
https://maxp2027.github.io/chicos-oven/

A small business website for Chico's Oven, built with Flask and Jinja2 templates. The site includes a home page, menu, donuts page, custom donuts gallery, about page, contact page, and legal pages (privacy policy and terms and conditions). A build script exports the site as static HTML so it can be hosted on GitHub Pages.

## Features
Dynamic page routing — All non-home pages are generated from a single PAGES dictionary in app.py, so adding a new page only requires one new entry and a template file.

Shared base template — base.html provides a consistent header, navigation bar, and footer across every page, with the active page highlighted in the nav using aria-current="page".

Responsive navigation — A collapsible mobile menu (nav-toggle) and a "More" dropdown for secondary links (Contact, Privacy Policy, Terms and Conditions).

Automatic image detection — A Flask context processor (image_file) checks for a logo and hero image across multiple file formats (.png, .jpg, .jpeg, .webp, .svg) and injects whichever one exists into every template.

Accessibility considerations — Includes a skip-to-content link, aria-label/aria-expanded attributes on interactive elements, and semantic HTML structure.

Static site export — build_preview.py renders every route to static HTML in a docs/ folder, rewrites internal links for static hosting, copies static assets, and validates that no links are broken and no template tags were left unrendered.

## Tech Stack
Backend: Python, Flask
Templating: Jinja2
Frontend: HTML, CSS, JavaScript
Deployment: Static export to GitHub Pages via a custom build script


