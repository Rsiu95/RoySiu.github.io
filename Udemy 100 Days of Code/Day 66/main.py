from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rand
import urllib



app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Udemy 100 Days of Code/Day 66/cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods = ["GET"])
def random_cafe():
    results = db.session.execute(db.select(Cafe)).scalars()
    all_cafes = results.all()
    random_cafe = rand.choice(all_cafes)
    print(random_cafe.to_dict())
    return jsonify(cafe = random_cafe.to_dict())

@app.route("/all", methods = ["GET"])
def all_cafes():
    results = db.session.execute(db.select(Cafe)).scalars()
    all_cafes = results.all()
    cafe_list = []
    for cafe in all_cafes:
        cafe_list.append(cafe.to_dict())
    return jsonify(all_cafes = cafe_list)

@app.route("/search", methods = ["GET"])
def search_cafe():
    results = db.session.execute(db.select(Cafe)).scalars()
    
    all_cafes = results.all()
    cafe_loc = request.args.get('loc')
    
    # using .where() call
    # result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_loc))
    
    cafe_list = []
    for cafe in all_cafes:
        if cafe.location == cafe_loc:
            cafe_list.append(cafe.to_dict())
    if len(cafe_list) != 0:
        return jsonify(all_cafes = cafe_list)
    else:
        return jsonify(error = {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }), 404

## HTTP POST - Create Record
@app.route("/add", methods = ["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
@app.route("/update_cafe/<int:cafe_id>", methods = ["PATCH"])
def update_cafe(cafe_id):
    cafe_to_update = db.get_or_404(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response = {"success": "Successfully updated the price."})
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})

## HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods = ["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = db.get_or_404(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response = {"success": "Successfully removed cafe."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


if __name__ == '__main__':
    app.run(debug=True)
