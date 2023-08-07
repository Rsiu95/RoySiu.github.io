from turtle import Screen
from random import choice
import time

import importlib
module_name = "Day 23 - Turtle Crossing Helper"
module = importlib.import_module(module_name)

screen_height = 500
screen_width = 700

RANDOM_COLOR = ["red", "blue", "purple", "green", "purple", "pink", "orange"]

screen = Screen()
screen.setup(screen_width, screen_height)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = module.Player()
scoreboard = module.Scoreboard()
car = module.Cars(choice(RANDOM_COLOR))

cars = []
count = 0
speed = 5

screen.listen()
screen.onkeypress(turtle.move_up, "w")
screen.onkeypress(turtle.move_left, "a")
screen.onkeypress(turtle.move_down, "s")
screen.onkeypress(turtle.move_right, "d")

playing = True
while playing:
    
    screen.update() 
    car_color = choice(RANDOM_COLOR)
    time.sleep(car.move_speed)

    car.move_car()
    
    # Handles adding more cars to be printed across the screen
    count += 1
    if count % 30 == 0 and len(cars) != 100:
        x = module.Cars(car_color)
        cars.append(x)
    
    # Handles behavior of each car    
    for c in cars:
        c.move_car()
        print(speed)
        # Check collision with player
        if turtle.ycor() > ((screen_height//2) - 30):
            scoreboard.increment_score()
            time.sleep(0.5)
            turtle.reset_position()
            c.increase_carspeed(speed)
            c.increase_speed(speed)
            speed += 100
            print("current speed:", speed)
            
        # reset the car position to right of screen
        if c.xcor() < -(screen_width//2):
            c.random_start_pos()
            
        # Handles car collision with player
        if c.distance(turtle) < 20:
            scoreboard.game_over()
            playing = False        
    
    # #car.spawn_newcar()
    # time.sleep(car.move_speed)
    
    # if turtle.ycor() > ((screen_height//2) - 30):
    #     scoreboard.increment_score()
    #     time.sleep(0.5)
    #     turtle.reset_position()
    #     car.increase_speed()
    
    # if car.xcor() < -(screen_width//2):
    #     car.random_start_pos()

    # if car.distance(turtle) < 30:
    #     scoreboard.game_over()
    #     playing = False        
screen.exitonclick()