
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
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    print("NEW LEAD:")
    print(name, email, message)

    return render_template("success.html", name=name)




if __name__ == "__main__":
    app.run