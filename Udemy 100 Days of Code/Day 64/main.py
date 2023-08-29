from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../Udemy 100 Days of Code/Day 64/movielist.db"

db = SQLAlchemy()
db.init_app(app)
Bootstrap5(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    release_date = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_comment = db.Column(db.String, nullable=False)
    movie_description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods = ["POST", "GET"])
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.title)).scalars()
    return render_template("index.html", movies = movies)

@app.route("/add", methods = ["POST", "GET"])
def add_movie():
    if request.method == "POST":
        movie = Movie(
            title = request.form["title"],
            release_date = request.form["release_date"],
            rating = request.form["rating"],
            review_comment = request.form["review_comment"],
            movie_description = request.form["movie_description"],
            image_url = request.form["image_url"]
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods = ["POST", "GET"])
def edit_movie(id):
    movie_to_update = db.get_or_404(Movie, id)
    if request.method == "POST":
        movie_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", id = id, movie_to_update = movie_to_update)

@app.route("/delete", methods=["POST", "GET"])
def delete_movie():
    if request.method == "GET":
        movie_id = request.args.get('id')  # Use request.args to get query parameters
        if movie_id:
            movie_to_delete = Movie.query.get_or_404(movie_id)
            db.session.delete(movie_to_delete)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
