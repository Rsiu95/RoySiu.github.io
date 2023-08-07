from turtle import Turtle
DOWN, UP = 270, 90

class Player:
    def __init__(self, start_pos):
        self.segment = []
        self.create_player(start_pos)
        self.paddle_head = self.segment[0]
        self.paddle_tail = self.segment[-1]
        
    def create_player(self, starting_position):
        for position in starting_position:
            self.add_segment(position)
    
    def add_segment(self, position):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(position)
        self.segment.append(paddle)
        
    def move_up(self):
        #if self.paddle_head.heading() != DOWN:
        if self.paddle_head.ycor() > 470:
            self.paddle_head.fd(0)
        else:
            for body in range(len(self.segment) - 1, 0, -1):
                new_y = self.segment[body - 1].ycor()
                self.segment[body].sety(new_y)
            self.paddle_head.setheading(UP) 
            self.paddle_head.fd(20)           

    def move_down(self):
        # move from tail to head, update position of tail to the position
        # of the body part in front.
        if self.paddle_tail.ycor() < -470:
            self.paddle_tail.fd(0)
        else:
            for body in range(0, len(self.segment) - 1, 1):
                new_y = self.segment[body + 1].ycor()
                self.segment[body].sety(new_y)
            self.paddle_tail.setheading(DOWN)
            self.paddle_tail.fd(20)
          

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    
    def set_random_start_direction(self):
        self.fd(10)
        self.setheading(90)
        self.fd(10)
        self.setheading(0)
    
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.05
        self.bounce_x()
        
    
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 380)
        self.write(f"{self.player1_score}", align = ALIGNMENT, font = FONT)
        self.goto(350, 380)
        self.write(f"{self.player2_score}", align = ALIGNMENT, font = FONT)
    
    def player1_increment_score(self):
        self.player1_score += 1
        self.update_scoreboard()
    
    def player2_increment_score(self):
        self.player2_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)
        
class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        
        self.hideturtle()
        self.penup()
        self.goto(0, 500)
        self.pensize(10)
        self.setheading(270)
        self.move()
        
    def move(self):
        for _ in range(50):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)