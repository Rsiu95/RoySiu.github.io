import time
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
time.sleep(1)
print("You have just arrived on shore of what seems to be a deserted island.")
time.sleep(1)
print("You and your crew begin to explore the island and find a path that ")
time.sleep(1)
print("looks to have been carved out previously. You follow this path until")
time.sleep(1)
print("you reach a cross road. The path splits into two. ")
path = input("Which path do you take, left or right? ")
if path != "left":
    time.sleep(1)
    print("You choose the right and continue along the path. Suddenly, the ground gives way!")
    time.sleep(1)
    print("You and your crew have fallen into a pitfall trap. You all perish! Game Over!")
    exit()
time.sleep(1)
print("You choose the left path and continue along the path. The scenery is magnificent, ")
time.sleep(1)
print("you absorb the sunlight as it shines on your face and come across a fast moving river.")
time.sleep(1)
print("You see no way across, but you notice that the water level is slowly decreasing. You")
time.sleep(1)
print("are quite confident with your swimming abilities and believe you and the crew can swim")
time.sleep(1)
print("across quite easily. It's still early in the day but you and your crew would need to wait")
time.sleep(1)
print("about 2 hours before the water levels are low enough for you to cross safely.")
time.sleep(1)
swim = input("Do you choose to swim or wait? ")
if swim != "wait":
    time.sleep(1)
    print("You and your crew jump in with excitement! You've built up a sweat and the water hitting your")
    time.sleep(1)
    print("body is quite refreshing. You feel something around your feet, you think nothing of it.")
    time.sleep(1)
    print("You've just crossed the halfway mark when suddenly a school of trout attack you and your crew!")
    time.sleep(1)
    print("You try to defend yourselves but it's too late! You and your crew perish! Game Over!")
    exit()
time.sleep(1)
print("You decide to wait the 2 hours and sit down for lunch instead. It's just past noon and you all place")
time.sleep(1)
print("your equipment over your head and start walking through the river. The water isn't cold, the temperature")
time.sleep(1)
print("is just right. You cross the river succesfully and find another path, leading you through the trees.")
time.sleep(1)
print("You continue down this path until you eventually lead to the base of a mountain where there are 3 giant")
time.sleep(1)
print("coloured metal doors Red, Blue, and Yellow. You stand there a moment to ponder which door to choose.")
time.sleep(1)
door = ""
door += input("Which door do you choose? Blue, Yellow or Red? ")
if door == "Red" or door == "red":
    time.sleep(1)
    print("You approach the red door, you place your hand on it. It feels warm. You and your crew push the doors open.")
    time.sleep(1)
    print("You venture in with your crew, the path becomes hotter as you get deeper into the cave. Suddenly the doors slam")
    time.sleep(1)
    print("shut! You're trapped! You see a bright light approaching you and your crew, the heat is intense! It's fire!!!")
    time.sleep(1)
    print("you and your crew run as fast as you can to try and open the red door but it's too late. You and your crew are")
    time.sleep(1)
    print("instantly incinerated. You and your crew have perished! Game Over!")
elif door == "Yellow" or door == "yellow":
    time.sleep(1)
    print("You approach the Yellow door, you place your hand on it. It feels warm. You and your crew push the doors open.")
    time.sleep(1)
    print("You venture in with your crew, the path becomes hotter as you get deeper into the cave. Suddenly the doors slam")
    time.sleep(1)
    print("shut! You're trapped! You do not care, you continue to walk through the cave. You see a light at the end of the tunnel.")
    time.sleep(1)
    print("You approach the end of the tunnel and in the centre of it is a chest. A golden chest. You approach it carefully, no traps.")
    time.sleep(1)
    print("You place your hand over it and attempt to open it, succes! You open the chest and reveal a chest full of gold coins!")
    time.sleep(1)
    print("You hear the sound of the front doors opening, you and your crew are ecstatic! You exit the way you came in and leave the island.")
    time.sleep(1)
    print("Congratulations! You've found the treasure!")
    exit()
elif door == "Blue" or door == "blue":
    time.sleep(1)
    print("You approach the blue door, you place your hand on it. It feels cold. You and your crew push the doors open.")
    time.sleep(1)
    print("You venture in with your crew, the path becomes colder as you get deeper into the cave. Suddenly the doors slam")
    time.sleep(1)
    print("shut! You're trapped! You see a bright light approaching you and your crew, the cold is intense! It's ice!!!")
    time.sleep(1)
    print("you and your crew run as fast as you can to try and open the red door but it's too late. You and your crew are")
    time.sleep(1)
    print("instantly frozen. You and your crew have perished! Game Over!")

else:
    time.sleep(1)
    print("You choose not to open any door and return home because you realise you're rich enough already. Game Over!")
    