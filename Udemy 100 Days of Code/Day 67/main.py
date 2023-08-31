from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date as dt
from datetime import datetime
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
Bootstrap5(app)
ckeditor = CKEditor(app)

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

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])    
    author = StringField("Author", validators=[DataRequired()])
    blog_url = StringField("Image URL", validators=[DataRequired()])
    body = CKEditorField("Body", validators=[DataRequired()])
    add_post = SubmitField('Add Post')
   
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

@app.route("/toppost")
def post_page():
    return render_template("toppost.html")

@app.route("/blogpost/<int:number>")
def blogpost_page(number):
    response = db.get_or_404(BlogPost, number)
    return render_template("blogpost.html", posts = response)

@app.route("/addpost", methods = ["POST","GET"])
def add_post():
    date_string = str(dt.today())
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    formatted_date = date_object.strftime("%d, %B %Y")
    form = PostForm()
    
    if form.validate_on_submit():
        new_post = BlogPost(
        title = request.form['title'],
        subtitle = request.form['subtitle'],
        date = formatted_date,
        body = request.form['body'],
        author = request.form['author'],
        img_url = request.form['blog_url']
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home_page'))
    return render_template("addpost.html", date = formatted_date, form = form)

@app.route("/editpost/<int:number>", methods = ["POST", "GET"])
def edit_post(number):
    post_to_update = db.get_or_404(BlogPost, number)
    post_to_edit = PostForm(
        title = post_to_update.title,
        subtitle = post_to_update.subtitle,   
        author = post_to_update.author,
        blog_url = post_to_update.img_url,
        body = post_to_update.body,
    )
    
    if post_to_edit.validate_on_submit():
        post_to_update.title = request.form['title']
        post_to_update.subtitle = request.form['subtitle']
        post_to_update.body = request.form['body']
        post_to_update.author = request.form['author']
        post_to_update.img_url = request.form['blog_url']
        db.session.commit()
        return redirect(url_for("blogpost_page", number = post_to_update.id))
    return render_template("addpost.html", form = post_to_edit, is_edit = True)

@app.route("/deletepost", methods = ["POST","GET"])
def delete_post():
    if request.method == "GET":
        print("did we get?")
        post_id = request.args.get('number')
        print(post_id)
        if post_id:
            post_to_delete = BlogPost.query.get_or_404(post_id)
            db.session.delete(post_to_delete)
            db.session.commit()
            return redirect(url_for('home_page'))
    return render_template("index.html")

    

if __name__ == "__main__":
    # debug = True to activate live code updates
    app.run(debug=True)