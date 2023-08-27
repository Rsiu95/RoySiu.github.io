from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps', validators=[URL()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=["☕️"*value for value in range(6)], validators=[DataRequired()])
    wifi = SelectField('WiFi Rating', choices=["💪"*value for value in range(6)], validators=[DataRequired()])
    power = SelectField('Power Outlet Rating', choices=["🔌"*value for value in range(6)], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["POST","GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(form.cafe.data)
        with open('Udemy 100 Days of Code/Day 62/cafe-data.csv', "a", newline='', encoding='utf-8') as csv_file:
            data = [form.cafe.data, form.location.data, form.open_time.data, form.close_time.data, form.coffee.data, form.wifi.data, form.power.data]
            csv_file.writelines("\n"+",".join(data))
        form = CafeForm()
        return render_template('add.html', form=form, msg_sent = True)
    return render_template('add.html', form=form, msg_sent = False)


@app.route('/cafes')
def cafes():
    with open('Udemy 100 Days of Code/Day 62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)    
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
