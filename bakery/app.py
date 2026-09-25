from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)


def image_file(stem):
    for extension in ('png', 'jpg', 'jpeg', 'webp', 'svg'):
        filename = f'images/{stem}.{extension}'
        if (Path(app.static_folder) / filename).is_file():
            return filename
    return None


@app.context_processor
def images():
    return {'logo_image': image_file('logo'), 'hero_image': image_file('home-page-img')}


@app.route('/')
def home():
    return render_template('home.html', title='Home', is_home=True)


PAGES = {
    'menu': ('menu.html', 'Menu'),
    'donuts': ('donuts.html', 'Donuts'),
    'custom-donuts-gallery': ('gallery.html', 'Custom Donuts Gallery'),
    'about-us': ('about.html', 'About Us'),
    'contact-us': ('contact.html', 'Contact Us'),
    'privacy-policy': ('privacy.html', 'Privacy Policy'),
    'terms-and-conditions': ('terms.html', 'Terms and Conditions'),
}


def page_view(template, title):
    def view():
        return render_template(template, title=title, is_home=False)
    return view


for slug, (template, title) in PAGES.items():
    app.add_url_rule(f'/{slug}', slug, page_view(template, title))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
