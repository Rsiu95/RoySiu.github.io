from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/<name>")
def age_check(name):
    
    AGE_URL = f"https://api.agify.io?name={name}"
    response = requests.get(AGE_URL)
    user_age = response.json()['age']
    
    GENDER_URL = f"https://api.genderize.io?name={name}"
    response = requests.get(GENDER_URL)
    gender = response.json()["gender"]
    
    current_year = dt.datetime.now().year
    print(current_year)
    return render_template("index.html", age = user_age, name = name, year = current_year, gender = gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(BLOG_URL)
    posts = response.json()
    return render_template("blog.html", posts = posts)

if __name__ == "__main__":
    # debug = True to activate live code updates
    app.run(debug=True)