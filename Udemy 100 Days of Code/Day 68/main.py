from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Udemy 100 Days of Code/Day 68/users.db'
db = SQLAlchemy()
db.init_app(app)

# CREATE LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))    
 
 
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")



@app.route('/register', methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        temp_password = request.form.get('password')
        hashed_password = generate_password_hash(temp_password, method="pbkdf2", salt_length=16)
        print(hashed_password)
        new_user = User(
            email = request.form.get('email'),
            password = hashed_password,
            name = request.form.get('name'),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            # return redirect(url_for('secrets', name = request.form.get('name')))
            login_user(new_user)
            return render_template('secrets.html')
        except:
            flash("Email already in use.")
            return redirect(url_for('login'))
    return render_template("register.html")




@app.route('/login', methods = ["POST", "GET"])
def login():
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        try:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('secrets'))
            if not check_password_hash(user.password, password):
                flash('Incorrect password.')
                return redirect(url_for('login'))
        except AttributeError:
            flash('No email found.')
            return redirect(url_for('login'))
        
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    # name = request.args.get('name')
    # return render_template("secrets.html", name = name)
    
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static', path = "files/cheat_sheet.pdf")
    

if __name__ == "__main__":
    app.run(debug=True)
