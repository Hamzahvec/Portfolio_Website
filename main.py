from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)
app.secret_key = "QWERtyu87%qwERtyHbfr$"

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    phone_no = TelField("Phone Number (Optional)")
    message = TextAreaField("Your Message", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    with open("projects-data.json") as file:
        data = json.load(file)
    return render_template("projects.html", data=data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        clean_message = BeautifulSoup(form.message.data, "html.parser").get_text()
        webhook_url = "https://discordapp.com/api/webhooks/1527581961005305857/_L_PSe-Q6gB1N2tws13pJjLw6WFPGwPpWRP3MTlXLHg5jNoRTIjeAUktwYoYWjTWDILd"
        payload = {
            "content": f"🚀 **New Contact!**\n**Name:** {form.name.data}\n**Email:** {form.email.data}\n\n**Message:** \n{clean_message}"
        }
        requests.post(webhook_url, json=payload)
        return render_template("thank_you_page.html")
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
