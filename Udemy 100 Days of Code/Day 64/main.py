from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, os
import pprint
from dotenv import load_dotenv

load_dotenv()
pp = pprint.PrettyPrinter(indent=4)
API_KEY = os.getenv("API_KEY")
READ_TOKEN = os.getenv("READ_TOKEN")

movie_url = "https://api.themoviedb.org/3/search/movie"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + READ_TOKEN,
}

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
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review_comment = db.Column(db.String, nullable=True)
    movie_description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

class MovieUpdateForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Update Review')


class AddMovie(FlaskForm):
    movie = StringField("Movie Title", validators=[DataRequired()])
    add = SubmitField('Find Movie')


with app.app_context():
    db.create_all()

@app.route("/", methods = ["POST", "GET"])
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars()
    
    # more efficient way to sort, we take the len of all movies, set its ranking to the length of list - its index
    # all_movies = movies.all()
    # for i in range(len(all_movies)):
    #     all_movies[i].ranking = len(all_movies) - i
    #     print(all_movies[i])
        
    movie_ratings = [[movie.rating, movie.id] for movie in movies]
    movie_ratings.sort()
    for index, movie in enumerate(movie_ratings):
        movie_to_update = db.get_or_404(Movie, movie[1])
        movie_to_update.ranking = index + 1
        db.session.commit()
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars()
    return render_template("index.html", movies = movies)

@app.route("/add", methods = ["POST", "GET"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        parameters = {
            'query': request.form['movie'],
        }
        response = requests.get(movie_url, headers=headers, params=parameters)
        movie_data = response.json()
        return render_template("select.html", movie_data = movie_data)
    return render_template("add.html", form = form)

@app.route("/edit/<int:id>", methods = ["POST", "GET"])
def edit_movie(id):
    form = MovieUpdateForm()
    movie_to_update = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review_comment = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", id = id, movie_to_update = movie_to_update, form = form)

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

@app.route("/find", methods = ["POST", "GET"])
def find_movie():
    movie_id = request.args.get("movie_id")
    print(movie_id)
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    parameters = {
        "movie_id": movie_id,
    }
    response = requests.get(url, headers=headers, params=parameters)
    print("HI", response)
    movie_data = response.json()
    pp.pprint(movie_data)
    new_movie = Movie(
        title = movie_data["original_title"],
        release_date = movie_data["release_date"].split("-")[0],
        image_url = f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{movie_data['poster_path']}",
        movie_description = movie_data["overview"],
        ranking = 0,
        rating = 0,
        review_comment = "temp"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_movie", id = new_movie.id))
    
if __name__ == '__main__':
    app.run(debug=True)
