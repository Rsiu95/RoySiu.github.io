from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../Udemy 100 Days of Code/Day 63/booklist.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", books=books)


@app.route("/add", methods = ["POST", "GET"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/update/<int:id>", methods = ["POST", "GET"])
def update_rating(id):
    book_to_update = db.get_or_404(Book, id)
    if request.method == "POST":
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("update.html", id = id, book_to_update = book_to_update)

@app.route("/delete", methods=["POST", "GET"])
def delete_book():
    if request.method == "GET":
        book_id = request.args.get('id')  # Use request.args to get query parameters
        if book_id:
            book_to_delete = Book.query.get_or_404(book_id)
            db.session.delete(book_to_delete)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("index.html")


    

if __name__ == "__main__":
    app.run(debug=True)

