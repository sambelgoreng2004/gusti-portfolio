from urllib.parse import quote_plus
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

projects = [
    {
        "title": "Web Portfolio Flask",
        "desc": "Personal portfolio website built using Flask and Jinja template.",
        "tech": "Python, Flask, HTML, CSS"
    },
    {
        "title": "Login System",
        "desc": "Authentication system with session management.",
        "tech": "Flask, SQLite"
    }
]

@app.route("/")
def home():
    return render_template("index.html", projects=projects)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    wa_number = os.environ.get("WA_NUMBER", "").strip()

    if not wa_number:
        return "WA_NUMBER not configured", 500

    text = (
        "Hello, I want to order a company website.\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Project Details: {message}"
    )

    encoded_text = quote_plus(text)
    wa_link = f"https://wa.me/{wa_number}?text={encoded_text}"

    return redirect(wa_link)


if __name__ == "__main__":
    app.run()
