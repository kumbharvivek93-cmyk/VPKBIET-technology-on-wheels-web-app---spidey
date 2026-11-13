# Technology on Wheels (ToW): VPKBIET

Flask website with a scroll-driven bus hero animation (CSS scroll-driven animations, JS fallback, `prefers-reduced-motion` respected).

## Setup
```bash
python -m venv venv
venv\Scripts\activate          # Windows   (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python app.py                  # open http://127.0.0.1:5000
```

## Folder structure
```
app.py                 routes + form handling
data.py                ALL editable text/content (nav, hero, about, activities, projects, contact, feedback)
templates/             base.html (navbar + footer) and one file per page
static/css/style.css   styling (colours are variables at the top)
static/js/main.js      menu, reveal, hero fallback, gallery filter, lightbox, form validation
static/img/gallery/    photos used in the gallery
submissions/           contact.json and feedback.json are created here on submit
```

## What to edit
- **Text:** `data.py`. Anything marked `EDITABLE` is a placeholder (phone, email, address, social links, age/duration of activities, timeline, sample feedback, placeholder projects).
- **Gallery photos:** put images in `static/img/gallery/` and add/edit an entry in `PROJECTS` in `data.py` (`"img": "file.jpg"`). Leave `"img": ""` to show an emoji icon instead.
- **Bus / background:** the bus and VPKBIET campus are inline SVG in `templates/index.html`. To use a real bus photo, replace the `<svg>` inside `<div class="bus">` with an `<img>`.
- **Colours:** `:root` variables at the top of `style.css`.
- **Secret key:** change `app.secret_key` in `app.py` before deploying.
