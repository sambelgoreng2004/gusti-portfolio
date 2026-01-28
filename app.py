from urllib.parse import quote_plus
from flask import session, redirect, url_for
from flask import Flask, render_template, request, redirect
import os
import sqlite3
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345"

app = Flask(__name__)
app.secret_key = "supersecretkey123"

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

import sqlite3

@app.route("/admin")
def admin():

    conn = sqlite3.connect("leads.db")
    c = conn.cursor()

    c.execute("SELECT * FROM leads ORDER BY id DESC")
    leads = c.fetchall()

    conn.close()

    return render_template("admin.html", leads=leads)


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    # =========================
    # SAVE TO DATABASE (TARUH DISINI)
    # =========================

    conn = sqlite3.connect("leads.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO leads (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    # =========================
    # WHATSAPP REDIRECT
    # =========================

    wa_number = os.environ.get("WA_NUMBER", "").strip()

    if not wa_number:
        return "WA_NUMBER not configured", 500

    text = (
        "Hello Gusti, I would like to order a company website.\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Project Details:\n{message}\n\n"
        "Please let me know the estimated price and timeline. Thank you."
    )

    encoded_text = quote_plus(text)

    wa_link = f"https://wa.me/{wa_number}?text={encoded_text}"

    return redirect(wa_link)

@app.route("/admin")
def admin():

    if not session.get("admin_logged"):
        return redirect("/admin/login")

    conn = sqlite3.connect("leads.db")
    c = conn.cursor()

    c.execute("SELECT * FROM leads ORDER BY id DESC")
    leads = c.fetchall()

    conn.close()

    return render_template("admin.html", leads=leads)

@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect("/admin/login")


if __name__ == "__main__":
    app.run()
