from turtle import Turtle, Screen
import colorgram
from random import choice

rgb_colors = []
colors = colorgram.extract('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 18/image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

screen = Screen()
screen.setup(500,500)
john = Turtle()
print(john.position())
john.ht()
john.pu()
x_pos = -200
y_pos = -200
john.setpos(x_pos,y_pos)

def reset_pos(x_pos, y_pos):
    pass
    

while True:
    print(john.position())
    john.st()
    random_colour = choice(rgb_colors)
    color_string = "#%02x%02x%02x" % random_colour
    john.dot(15,color_string)
    john.fd(20)
    x_pos += 20
    if x_pos == 200:
        john.ht()
        john.pu
        y_pos += 20
        x_pos = -200
        john.setx(-200)
        john.sety(y_pos)
        
    if y_pos == 220:
        screen.exitonclick()
    