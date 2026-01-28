from flask_mail import Mail, Message
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'EMAILKAMU@gmail.com'
app.config['MAIL_PASSWORD'] = 'APP_PASSWORD_GMAIL'
mail = Mail(app)

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

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    msg = Message(
        subject="New Website Order Request",
        sender=email,
        recipients=["EMAILKAMU@gmail.com"]
    )

    msg.body = f"""
New Client Inquiry

Name: {name}
Email: {email}
Message:
{message}
"""

    mail.send(msg)

    return "Message Sent Successfully!"


if __name__ == "__main__":
    app.run(debug=True)