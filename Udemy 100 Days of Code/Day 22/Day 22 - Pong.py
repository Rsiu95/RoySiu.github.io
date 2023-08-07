from turtle import Screen
from time import sleep

import importlib
module_name = "Day 22 - Pong_Helper"
module = importlib.import_module(module_name)

screen = Screen()
screen.setup(width = 1400, height = 1000)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1_startpos = [(-620, 50), (-620, 30), (-620, 10), (-620, -10), (-620, -30), (-620, -50)]
player2_startpos = [(620, 50), (620, 30), (620, 10), (620, -10), (620, -30), (620, -50)]

# Create game objects
player1 = module.Player(player1_startpos)
player2 = module.Player(player2_startpos)
ball = module.Ball()
middle_line = module.Midline()
    
scoreboard = module.Scoreboard()

# Detects movement
screen.listen()

# Player 1 movement
screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")

# Player 2 movement
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")

playing = True

while playing:
    screen.update()
    sleep(ball.move_speed)
    ball.move_ball()
    
    # check collision with top/bottom edge
    if ball.ycor() > 470 or ball.ycor() < -470:
        ball.bounce_y()
    
    if ball.xcor() > 670:
        ball.reset_position()
        scoreboard.player1_increment_score()
        
    elif ball.xcor() < -670:
        ball.reset_position()
        scoreboard.player2_increment_score()
        
    # check collision with paddle player 1
    for seg in player1.segment:
        if ball.distance(seg) < 30 and ball.xcor() < 630:
            ball.bounce_x()
    
    # check collision with paddle player 2
    for seg in player2.segment:
        if ball.distance(seg) < 30 and ball.xcor() > -630:
            ball.bounce_x()    
    
screen.exitonclick()