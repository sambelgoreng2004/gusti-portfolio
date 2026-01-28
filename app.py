from flask import Flask, render_template, request, redirect
from urllib.parse import quote_plus
import os

app = Flask(__name__)

# -------------------------------
# PROJECT DATA
# -------------------------------

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


# -------------------------------
# HOME PAGE
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html", projects=projects)


# -------------------------------
# CONTACT FORM → WHATSAPP REDIRECT
# -------------------------------

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    wa_number = os.environ.get("WA_NUMBER", "").strip()

    if not wa_number:
        return "WhatsApp number not configured", 500

    wa_text = (
        "Hello, I would like to order a company website.\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Project Details:\n{message}"
    )

    encoded_text = quote_plus(wa_text)

    wa_link = f"https://wa.me/{wa_number}?text={encoded_text}"

    return redirect(wa_link)



# -------------------------------
# RUN LOCAL SERVER
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
