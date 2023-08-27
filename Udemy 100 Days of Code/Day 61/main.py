from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap5


def validate_email(form, field):
    if "@" not in str(field):
        raise ValidationError("Not a valid email address.")

    at_index = str(field).find("@")
    if "." not in str(field)[at_index:]:
        raise ValidationError("Not a valid email address.")
    
    string_after_at = str(field)[at_index:]

    dot_index = string_after_at.find(".")
    if len(string_after_at[dot_index:]) < 4:
        raise ValidationError("Not a valid email address.")

class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), validate_email])
    password = PasswordField('Password', validators=[InputRequired()])
    def validate_password(form, field):
        if len(field.data) < 8:
            raise ValidationError("Password must be at least eight characters long.")
    submit = SubmitField('Login')
    


app = Flask(__name__)
boostrap = Bootstrap5(app)
app.secret_key = "hey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST","GET"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        correct_email = "admin@email.com"
        correct_password = "12345678"
        if form.email.data == correct_email and form.password.data == correct_password:
            return redirect("/success")
        else:
            return redirect("denied.html")
    return render_template('login.html', form = form)

@app.route("/success", methods=["POST", "GET"])
def success():
    return render_template("success.html")

@app.route("/denied", methods=["POST", "GET"])
def denied():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)


