import json, re
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash
import data

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # change before deploying
SUB = Path(__file__).parent / "submissions"
SUB.mkdir(exist_ok=True)
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.context_processor
def inject():
    return dict(site=data.SITE, nav=data.NAV, contact=data.CONTACT)


def save(name, row):
    f = SUB / f"{name}.json"
    rows = json.loads(f.read_text("utf-8")) if f.exists() else []
    rows.append({**row, "submitted_at": datetime.now().isoformat(timespec="seconds")})
    f.write_text(json.dumps(rows, indent=2, ensure_ascii=False), "utf-8")


def handle(kind, required, endpoint, extra=None):
    """Validate a form, save it to submissions/<kind>.json, flash a message."""
    form = {k: request.form.get(k, "").strip() for k in required + (extra or [])}
    errors = {k: "This field is required." for k in required if not form[k]}
    if form.get("email") and not EMAIL.match(form["email"]):
        errors["email"] = "Enter a valid email address."
    if kind == "feedback" and form.get("rating") not in list("12345"):
        errors["rating"] = "Please choose a rating."
    if errors:
        return render_template(f"{kind}.html", errors=errors, form=form, samples=data.FEEDBACK_SAMPLES), 400
    save(kind, form)
    flash("Thank you! Your message has been received." if kind == "contact" else "Thank you for your feedback!")
    return redirect(url_for(endpoint) + "#form")


@app.route("/")
def index():
    return render_template("index.html", d=data)


@app.route("/about")
def about():
    return render_template("about.html", d=data)


@app.route("/learning-activities")
def learning_activities():
    return render_template("learning_activities.html", d=data)


@app.route("/project-gallery")
def project_gallery():
    cats = list(dict.fromkeys(p["cat"] for p in data.PROJECTS))
    return render_template("project_gallery.html", projects=data.PROJECTS, cats=cats)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return handle("contact", ["name", "email", "message"], "contact", ["phone", "school"])
    return render_template("contact.html", errors={}, form={})


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        return handle("feedback", ["name", "email", "role", "rating", "message"], "feedback", ["school"])
    return render_template("feedback.html", errors={}, form={}, samples=data.FEEDBACK_SAMPLES)


if __name__ == "__main__":
    app.run(debug=True)
