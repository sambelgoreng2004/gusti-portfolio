
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


from urllib.parse import quote

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    wa_text = f"""
Hello, I want to order a company website.

Name: {name}
Email: {email}
Project Details:
{message}
"""

    wa_text_encoded = quote(wa_text)

    wa_link = f"https://wa.me/6289894188382?text={wa_text_encoded}"

    return render_template("success.html", wa_link=wa_link, name=name)





if __name__ == "__main__":
    app.run