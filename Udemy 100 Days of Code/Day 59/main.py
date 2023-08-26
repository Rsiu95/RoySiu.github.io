from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = response.json()
print(blog_data)

@app.route("/")
@app.route("/index")
def home_page():
    return render_template("index.html", posts = blog_data)


@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

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