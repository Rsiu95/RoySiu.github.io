from flask import Flask, render_template, request, redirect, url_for
import requests, smtplib, os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = response.json()
#print(blog_data)

@app.route("/")
@app.route("/index")
def home_page():
    return render_template("index.html", posts = blog_data)


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
    return render_template("blogpost.html", posts = blog_data[number])




if __name__ == "__main__":
    # debug = True to activate live code updates
    app.run(debug=True)