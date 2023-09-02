from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
import requests, smtplib, os
from dotenv import load_dotenv
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm

# Environment Variables
load_dotenv()
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Udemy 100 Days of Code/Day 69/instance/posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# Register route
@app.route('/register', methods = ["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        # Check for existing username
        used_username = db.session.execute(db.select(User).where(User.username == request.form.get('username')))
        user = used_username.scalar()
        if user:
            flash("Username already exists.")
            return redirect(url_for('register', logged_in=current_user.is_authenticated))        
        
        # Check for existing email
        used_email = db.session.execute(db.select(User).where(User.email == request.form.get('email')))
        user_email = used_email.scalar()
        if user_email:

            flash("Email already exists.")
            return redirect(url_for('register', logged_in=current_user.is_authenticated))
        
        temp_password = request.form.get('password')
        # Use Werkzeug to hash the user's password when creating a new user.
        hashed_password = generate_password_hash(temp_password, method="pbkdf2", salt_length=16)
        new_user = User(
            first_name = request.form.get('fname'),
            last_name = request.form.get('lname'),
            username = request.form.get('username'),
            email = request.form.get('email'),
            password = hashed_password
        )
       
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))
       
            
    return render_template("register.html", form = form, logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        result = db.session.execute(db.select(User).where(User.username == username))
        user_username = result.scalar()
        
        if not user_username:
            flash("No such Username, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user_username.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for('login'))
        else:
            login_user(user_username)
            return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))
        
    return render_template("login.html", form = form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))


@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)


@app.route("/contact", methods=["GET", "POST"])
def contact():
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
        
        return render_template("contact.html", msg_sent = True, logged_in=current_user.is_authenticated)
    return render_template("contact.html", msg_sent = False, logged_in=current_user.is_authenticated)


if __name__ == "__main__":
    app.run(debug=True)
