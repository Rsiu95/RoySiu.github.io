from game_data import data
from art import logo, vs
import random
import os

# function to clear terminal
def clear_terminal():
    os.system("cls")

score = 0
    
def retrieve_random_data(random_data):
    return random.choice(random_data)

compare_a = retrieve_random_data(data)
compare_b = retrieve_random_data(data)

playing = True

while playing:
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
        
    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(vs)
    print(f"Against B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}")
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if compare_a['follower_count'] > compare_b['follower_count'] and user_input == "a":
        score += 1
        compare_b = retrieve_random_data(data)
    elif compare_a['follower_count'] < compare_b['follower_count'] and user_input == "b":
        score += 1
        compare_a = compare_b
        compare_b = retrieve_random_data(data)
    else:
        clear_terminal()
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        playing = False
    