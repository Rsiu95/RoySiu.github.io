from turtle import Turtle
from random import choice, randint

SCREEN_Y_BOUNDS = (-230, 220)
SCREEN_X_BOUNDS = (-330, 320)
START_POSITION = (0, -230)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(START_POSITION)
        self.setheading(90)
        self.showturtle()
        self.x_move = 0
        
    def move_up(self):
        if self.ycor() > SCREEN_Y_BOUNDS[1]:
            self.fd(0)
        else:
            self.fd(20)
        
    def move_down(self):
        if self.ycor() < SCREEN_Y_BOUNDS[0]:
            self.bk(0)
        else:
            self.bk(20)
        
    def move_right(self):
        current_y = self.ycor()
        if self.xcor() > SCREEN_X_BOUNDS[1]:
            self.goto(self.xcor() + 0,  current_y)
        else:
            
            self.goto(self.xcor() + 20,  current_y)
        
    def move_left(self):
        current_y = self.ycor()
        if self.xcor() < SCREEN_X_BOUNDS[0]:
            self.goto(self.xcor(),  current_y)
        else:
            self.goto(self.xcor() - 20,  current_y)
    
    def reset_position(self):
        self.goto(START_POSITION)
        
class Cars(Turtle):
    def __init__(self, car_color):
        super().__init__()
        self.shape("square")
        self.color(car_color)
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.penup()
        self.x_move = 5
        self.move_speed = 0.05
        self.random_start_pos()
    
    #def create_car(self, car_color):

    def move_car(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor()
        self.goto(new_x, new_y)
        
    def increase_carspeed(self, random_speed):
        #self.move_car()
        self.x_move + random_speed
        
    def increase_speed(self, speed):
        self.move_speed *= speed
    
    def random_start_pos(self):
        start_positions = (370, randint(-200, 220))
        self.goto(start_positions)

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")        

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-330, 210)
        self.write(f"Level: {self.score}", align = ALIGNMENT, font = FONT)
    
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font = FONT)