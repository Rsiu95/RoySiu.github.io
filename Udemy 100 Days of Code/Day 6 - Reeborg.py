#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdles 1 and 2
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    jump()

# Hudrles 3 and 4

def face_north():
    while not is_facing_north():
        turn_left()
    
while not at_goal():
    if right_is_clear() and not front_is_clear():
        turn_right()
        move()
    if not front_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

    if front_is_clear():
        move()
        
# Maze
# first attempt, works for some but not all.
while not at_goal():       
    if right_is_clear() and not front_is_clear():
        turn_right()
        move()
    if not front_is_clear():
        turn_left()
        print(turn_left())
    if right_is_clear():
        turn_right()

    if front_is_clear():
        move()
        print(right_is_clear())

# solution:

while front_is_clear():
    move()

while not at_goal():       
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
from library import turn_right
from library import jump
#from library import left_is_clear

while front_is_clear():
    move()

while not at_goal():       
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''

s = "23"
leading = "0."
leading + s
print(leading+s)