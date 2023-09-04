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
from sqlalchemy import ForeignKey
import smtplib, os
from dotenv import load_dotenv
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

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

# Configure Tables
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    
    # Create relationship between comments and blogposts for user ids that create posts
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comments", back_populates="comment_author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    img_url = db.Column(db.String(250), nullable=False)
    
    # Create relationship between blogpost and corresponding comments
    comments = relationship("Comments", back_populates="parent_post")

class Comments(db.Model):
    __tablename__ = "user_comments"
    id = db.Column(db.Integer, primary_key=True)
    
    # Create relationship between users and comments
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    
    # Create relationship between comments and blogpost
    parent_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    body = db.Column(db.Text)   

# Default gravatar setup
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# Protect html links with admin only    
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.get_id() == "1":
            return f(*args, **kwargs)
        return abort(403)
    return decorated_function

# Create database
with app.app_context():
    db.create_all()

# Enable login manager
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# Register route for user registration
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
        
        # Use Werkzeug to hash the user's password when creating a new user.
        temp_password = request.form.get('password')
        hashed_password = generate_password_hash(temp_password, method="pbkdf2", salt_length=16)
        
        # Create new user
        new_user = User(
            first_name = request.form.get('fname'),
            last_name = request.form.get('lname'),
            username = request.form.get('username'),
            email = request.form.get('email'),
            password = hashed_password
        )

        # Add user to db
        db.session.add(new_user)
        db.session.commit()
        
        # log the user in
        login_user(new_user)
        return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))
       
    return render_template("register.html", form = form, logged_in=current_user.is_authenticated)


# Retrieve a user from the database based on their username. 
@app.route('/login', methods = ["POST", "GET"])
def login():
    form = LoginForm()
    
    # Check if login button is clicked
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # find the user based on username
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

# Default logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))

# Homepage, retrieves all posts in current DB
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()

    if current_user.is_authenticated and current_user.get_id() == "1":
        return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, admin = True)
        
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated)


# View current post based on post id
@app.route("/post/<int:post_id>", methods = ["POST","GET"])
def show_post(post_id):
    # Retrieve the post based on post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    # Retrieve the comments tied to the post
    post_comments = requested_post.comments
    # intialise the form
    form = CommentForm()
    
    # check admin status, id == 1
    is_admin = False
    if current_user.get_id() == "1":
        is_admin = True

    # on click, check if user is authenticated (could use an "AND" statement)        
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comment = request.form.get("comment_field")
            new_comment = Comments(
                body = comment,
                author_id = current_user.get_id(),
                parent_id = post_id
                )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for("show_post", post_id = requested_post.id, post=requested_post, logged_in=current_user.is_authenticated, form = form, is_admin = is_admin,
                                   post_comments = post_comments))
            
        # Reject commenting if not logged in        
        else:
            flash("Please log in or register to comment")
            return redirect(url_for('login'))
        
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, form = form, is_admin = is_admin,
                                   post_comments = post_comments)


# New-post route for users to create posts, currently admin only
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
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
    return render_template("make-post.html", form=form, logged_in=current_user.is_authenticated)


# edit-post route for users to create posts, currently admin only
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
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


# delete-post route for users to create posts, currently admin only
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts', logged_in=current_user.is_authenticated))

# Link to about page 
@app.route("/about")
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)

# Link to contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")
        
        # send email to myself if user contacts me
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
    app.run(debug=False)
