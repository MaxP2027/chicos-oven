# Bakery Flask starter

## Start on Windows

Open this bakery folder in VS Code using File > Open Folder. Open a new terminal here:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

If `py` is unavailable, install Python 3 from python.org with the PATH option enabled, reopen VS Code, and use `python` in place of `py`.

Open http://127.0.0.1:5000 in your browser. Stop the server with Ctrl+C.

## Why a template may look unstyled or inaccessible

Do not double-click files in templates or open them using file:// or Live Server. Flask must render the templates and resolve `url_for` into real CSS, JavaScript, image, and page URLs. Open the localhost address while the Python server is running. All navigation uses Flask routes, not local HTML file paths.

## Files

- app.py: Flask application and all eight page routes.
- templates/base.html: shared header, dropdown, footer, CSS and JavaScript links.
- templates/home.html: full-screen hero and 50/50 Chocolate Donut section.
- templates/menu.html, donuts.html, gallery.html, about.html, contact.html, privacy.html, terms.html: individual editable pages.
- static/css/style.css: all styling and responsive layouts.
- static/js/main.js: scroll behavior and navigation dropdowns.
- static/images/: add logo.png and home-page-img.jpg (other supported extensions work too).

The supplied logo is included. Add home-page-img.jpg to static/images for the homepage photo. Until then the hero has a solid brown background. Marketing copy is placeholder text. Legal pages and contact details are intentionally unfinished placeholders; no contact form is connected.

The desktop logo starts at 25vw and shrinks to 10vw (60% smaller) after 30px of scrolling. Mobile uses 45vw and 18vw for readability. The header stays fixed, with white text; its background becomes rgba(0,0,0,0.6) after scrolling past the hero. Only the background is translucent, so text remains fully visible.

The right half of the Chocolate Donut section is blank. To add its image, place a file in static/images, then insert an img in the feature-image div using Flask's url_for helper, and style it with width:100%; height:100%; object-fit:cover.

This is a local development skeleton. Debug mode is enabled only by the direct app.py launcher; do not use that development server for public hosting.

