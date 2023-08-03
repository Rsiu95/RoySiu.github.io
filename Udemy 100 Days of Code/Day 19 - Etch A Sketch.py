from turtle import Turtle, Screen

john = Turtle()
screen = Screen()

screen.setup(500,500)


drawing = True

def move_forward():
    john.fd(10)

def move_backward():
    john.bk(10)

def turn_left():
    john.lt(10)

def turn_right():
    john.rt(10)


def clear_screen():
    john.clear()
    john.penup()
    john.home()
    john.pendown()

screen.listen()
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear_screen, "space")
screen.exitonclick()
    
