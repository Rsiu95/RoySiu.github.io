from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import requests, smtplib, os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Udemy 100 Days of Code/Day 67/posts.db'
db = SQLAlchemy()
db.init_app(app)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = response.json()

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/index")
def home_page():

    response = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars()

    all_posts = response.all()
    posts = [{"id": post.id,
                "title": post.title,
                "subtitle": post.subtitle,
                "date": post.date,
                "body": post.body, 
                "author": post.author,
                "img_url": post.img_url} for post in all_posts]
    print(all_posts)
    return render_template("index.html", posts = posts)


@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        print(f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")
        
        connection = smtplib.SMTP("smtp.gmail.com", port = 587)
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = MY_EMAIL,
            msg = f"Subject: BLOG CONTACT INFO \n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        )
        
        return render_template("contact.html", msg_sent = True)
    return render_template("contact.html", msg_sent = False)

@app.route("/post")
def post_page():
    return render_template("post.html")

@app.route("/blogpost/<int:number>")
def blogpost_page(number):
    number -= 1
    response = db.session.execute(db.select(BlogPost).order_by(BlogPost.date)).scalars()

    all_posts = response.all()

    posts = [{"id": post.id,
                "title": post.title,
                "subtitle": post.subtitle,
                "date": post.date,
                "body": post.body, 
                "author": post.author,
                "img_url": post.img_url} for post in all_posts]
    
    def get_post_by_id():
        for index, post in enumerate(posts):
            if post['id'] == number:
                return posts[index]
    a = get_post_by_id()
    print(a, number)
    return render_template("blogpost.html", posts = get_post_by_id())




if __name__ == "__main__":
    # debug = True to activate live code updates
    app.run(debug=True)