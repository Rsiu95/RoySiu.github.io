logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/  /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

import random

random_number = random.randint(1,100)
playing = True

def choose_difficulty(random_number, difficulty):
    if difficulty == "easy":
        turns = 10
    else:
        turns = 5
        
    print(f"You have {turns} attempts remaining to guess the number.")
    
    while turns > 0:
        turns -= 1
        
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.\nGuess again.")
        elif guess < random_number:
            print("Too low.\nGuess again.")
        elif guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        
        if turns > 0:
            print(f"You have {turns} attempts remaining to guess the number.")            
        else:
            print("You've run out of guesses, you lose.")
            break
    
while playing:
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {random_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "easy" or difficulty == "hard":
        choose_difficulty(random_number, difficulty)
        playing = False
    else:
        print("Please input either easy or hard.")
        playing = False