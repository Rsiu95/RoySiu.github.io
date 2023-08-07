from turtle import Turtle
from random import randint
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "Snake_Highscores.txt")

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_boddy(position)

    def add_boddy(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.shapesize(0.5)
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)
    
    def extend_body(self):
        self.add_boddy(self.snake_body[-1].position())
        
    def move(self):
        # move from tail to head, update position of tail to the position
        # of the body part in front.
        for body in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.snake_body[0].fd(MOVE_DISTANCE)
        
    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
            
    def snake_reset(self):
        for body in self.snake_body:
            body.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x, random_y = randint(-280, 280), randint(-280, 280)
        self.goto(random_x, random_y)

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file_path) as file:
            self.HIGHSCORE = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.HIGHSCORE}", align = ALIGNMENT, font = FONT)
    
    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def reset_scoreboard(self):
        if self.score > int(self.HIGHSCORE):
            self.HIGHSCORE = self.score
            with open(file_path, mode = "w") as file:
                file.write(f"{self.HIGHSCORE}")
        self.score = 0
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)