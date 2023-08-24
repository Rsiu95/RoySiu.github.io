from flask import Flask
import random


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Guess a number in the path of the URL! <br></br>i.e. 127.0.0.1:5000/1 <--- insert a number here</h1>"\
        '<div align="center"><img src="https://media.giphy.com/media/3ohk6AkkOXXeaC0bjq/giphy.gif"></div>'

correct_number = random.randint(1, 9)

# def make_bold(function):
#     def bold_text():
#         return "<b>" + function() + "</b>"
#     return bold_text

# def make_emphasised(function):
#     def emphazise_text():
#         return "<em>" + function() + "</em>"
    
#     return emphazise_text

# def make_underlined(function):
#     def underline_text():
#         return "<u>" + function() + "</u>"
#     return underline_text

# @app.route("/bye")
# @make_bold
# @make_emphasised
# @make_underlined
# def greet():
#     return "Bye!"

#     Low       '<p><img src="https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif"></p>'
#     High            '<p><img src="https://media.giphy.com/media/mxPzDgzRCKOty/giphy.gif"></p>'
#    Right'<p><img src="https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif"></p>'

# def style_my_text(function):
#     def give_css_style(*args, **kwargs):
#         return '<h1 style="text-align: center">' + function(*args, **kwargs) + '</h1>'
#     return give_css_style

# def style_my_image(function):
#    def image_style(*args, **kwargs):
#        value = function(*args, **kwargs)
#        if "low" in value:
#            return '<p><img src="https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif"></p>'
#        elif "high" in value:
#            return '<p><img src="https://media.giphy.com/media/mxPzDgzRCKOty/giphy.gif"></p>'
#        else:
#            return '<p><img src="https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif"></p>'
#    return image_style

@app.route("/<int:number>")
def a_number(number):
    if number < correct_number:
        return '<h1 style="text-align: center; color: blue">' + "Sorry, too low!" + '</h1>'+\
            '<div align="center"><img src="https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif"></div>'
    elif number > correct_number:
        return '<h1 style="text-align: center; color: red">' + "Sorry, too high!" + '</h1>'+\
            '<div align="center"><img src="https://media.giphy.com/media/mxPzDgzRCKOty/giphy.gif"></div>'
    else:
        return '<h1 style="text-align: center; color: purple">' + f"Correct! The answer was {correct_number}." + '</h1>'+\
            '<div align="center"><img src="https://media.giphy.com/media/IwAZ6dvvvaTtdI8SD5/giphy.gif"></div>'
    
if __name__ == "__main__":
    # debug = True to activate live code updates
    app.run(debug=True)