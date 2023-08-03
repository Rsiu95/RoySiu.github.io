from turtle import Turtle, Screen
from random import choice, randint

def create_turtles():
    turtles = []
    colors = ["red", "blue", "green", "black", "purple", "orange"]
    for turtle in range(6):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.shapesize(2)
        random_color = choice(colors)
        turtle.color(random_color)
        colors.remove(random_color)
        turtles.append(turtle)
    return turtles

def get_start_pos(turtle_list):
    start_pos = []
    y_pos = -280
    for _ in turtle_list:
        x_pos = -235
        y_pos += 80
        start_pos.append((x_pos,y_pos))
    return start_pos

def set_start_pos(turtle_list, position_list):
    for index, turtle in enumerate(turtle_list):
        turtle.penup()
        turtle.goto(position_list[index])

def set_turtle_speed(turtle_list):
    for index in range(len(turtle_list)):
        turtle_list[index].fd(randint(1,15))
        screen.delay(50)
        
screen = Screen()
screen.setup(width = 500, height = 500)
screen.title("Turtle Racing")
turtles = create_turtles()
starting_positions = get_start_pos(turtles)
set_start_pos(turtles, starting_positions)
user_input = screen.textinput("Which turtle will win? (Red/Blue/Green/Yellow/Purple/Orange)","Color: ").lower()




while True:
    set_turtle_speed(turtles)
    for turtle in turtles:
        if turtle.pos()[0] > 200:
            if user_input == turtle.color()[0]:
                print("Congratulations! You win!")
                text = Turtle()
                text.color("black")
                text.hideturtle()
                text.penup()
                text.goto(0,0)
                text.write("You won!", align="center", font=("Arial", 16, "normal"))
                #turtle.write("Contragrulations! You won! Try again!", align="center", font=("Arial", 16, "normal"))
            else:
                print(f"{turtle.color()[0]}, won! Try again!")
                text = Turtle()
                text.color("black")
                text.hideturtle()
                text.penup()
                text.goto(0,0)
                text.write(turtle.color()[0] + " won! Try again!", align="center", font=("Arial", 16, "normal"))
                #turtle.write(turtle.color()[0]+" won! Try again!", align="center", font=("Arial", 16, "normal"))
            screen.exitonclick()
