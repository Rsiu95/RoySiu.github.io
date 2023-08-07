from turtle import Screen
from time import sleep

import importlib
module_name = "Day 24 - Snake_Highscores_Helper"
module = importlib.import_module(module_name)


# Screen initialiser
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Creates the game objects
snake = module.Snake()
food = module.Food()

# Detects movement
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

playing = True
scoreboard = module.Scoreboard()
   
# Main game loop
while playing:
    screen.update()
    sleep(0.05)
    snake.move()
    scoreboard
    
    # Detect food eaten
    if snake.snake_head.distance(food) < 12:
        food.refresh()
        snake.extend_body()
        scoreboard.increment_score()

    # Detect wall collisions
    if snake.snake_head.xcor() < -295 or snake.snake_head.xcor() > 295 or \
        snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295:
        scoreboard.reset_scoreboard()
        snake.snake_reset()
        screen.update()
       # scoreboard.game_over()
       # playing = False
    
    
    # Detect collision with tail.
    for segment in snake.snake_body[1:]:
        if snake.snake_head.distance(segment) < 5:
            scoreboard.reset_scoreboard()
            snake.snake_reset()
            screen.re
        #    playing = False
        #    scoreboard.game_over()
    
screen.exitonclick()