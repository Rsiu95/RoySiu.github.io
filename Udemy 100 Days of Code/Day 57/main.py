from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = response.json()


@app.route('/')
def home():

    print(blog_posts)
    return render_template("index.html", posts = blog_posts)


@app.route('/blog/<int:number>')
def blog_page(number):
    number -= 1
    return render_template('post.html', post = blog_posts[number])

if __name__ == "__main__":
    app.run(debug=True)
