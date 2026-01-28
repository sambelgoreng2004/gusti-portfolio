from urllib.parse import quote
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
import os


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
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        wa_number = os.environ.get("WA_NUMBER")

        if not wa_number:
            print("ERROR: WA_NUMBER not found in ENV")
            return "Server config error. Please contact admin.", 500

        wa_text = f"""
Hello, I want to order a company website.

Name: {name}
Email: {email}
Project Details:
{message}
"""

        wa_text_encoded = quote(wa_text)

        wa_link = f"https://wa.me/{wa_number}?text={wa_text_encoded}"

        return render_template("success.html", wa_link=wa_link, name=name)

    except Exception as e:
        print("CONTACT ERROR:", e)
        return "Internal error", 500





if __name__ == "__main__":
    app.run