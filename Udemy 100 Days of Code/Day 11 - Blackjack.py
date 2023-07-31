logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#print(logo)

import random
import os

# function to clear terminal
def clear_terminal():
    os.system("cls")

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def convert_card(card):
    if card == "A":
        return [1, 11]
    elif card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return card

def get_cards(cards):
    random_card1 = random.randint(0,12)
    random_card2 = random.randint(0,12)
    return [cards[random_card1],cards[random_card2]]
#print(get_cards(cards))

def calculate_score(cards):
    card_values = []
    # convert our cards from Faces/Ace cards to their given values

    for card in cards:
        card_values.append(convert_card(card))

    score = 0
    # probably an easier way to check, but this was a bit of a hack
    # checks if there is [1, 11] at any given point
    if "[1, 11]" in str(card_values):
        temp_indices = []
        score_no_aces = 0
        # separate the indices that contain the Ace values
        for card in range(len(card_values)):
            if card_values[card] == [1, 11]:
                temp_indices.append(card)
            else:
                score_no_aces += card_values[card]

        for idx in temp_indices:
            ace = 0
            for val in card_values[idx]:

                if score_no_aces + val > 21:
                    ace = 1
                else:
                    ace = 11
                    
            # update our current score to include the new ace values
            score_no_aces = score_no_aces + ace
            
            # hack fix for if we go over with aces?
            if score_no_aces > 21:
                score_no_aces -= 10
                
        score = score + score_no_aces
        
        return score
            
    else:
        score += sum(card_values)
        return score
# cards2 = []
# for _ in range(21):
#     cards2.append("A")
# print(cards2)
# print(calculate_score(cards2))
# cards2 = ["A","A","A","A",5,"A"]
# print(calculate_score(cards2))
def restart_game(string):
    if string == "y":
        clear_terminal()
        print(logo)
    elif string == "n":
        playing == False
    

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
if start_game == "y":
    playing = True
    print(logo)
else:
    playing = False

while playing:
    player_cards = get_cards(cards)
    player_score = calculate_score(player_cards)

    computer_card = get_cards(cards)
    
    print(f"Your cards: {player_cards}, current score: {player_score}")
    
    # handles player blackjack
    if player_score == 21:
        print("Blackjack! Congratulations\n")
        replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if replay == "y":
            clear_terminal()
            print(logo)
            break                   
        elif replay == "n":
            playing = False
            break
    
    print(f"Computer's first card: {computer_card[0]}\n")
    
    # second loop to handle "hit"
    while True:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            player_cards.append(cards[random.randint(0,12)])
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_card[0]}\n")
            if player_score > 21:
                print(f"Your final hand: {player_cards}, your final score: {player_score}")
                print("You went over. You lose!")
                replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                if replay == "y":
                    clear_terminal()
                    print(logo)
                    break                   
                elif replay == "n":
                    playing = False
                    break
            
        elif hit == "n":
            print(f"\nYour cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_card[0]}")
            
            computer_score = calculate_score(computer_card)
            while computer_score < 17:
                new_card = cards[random.randint(0, 12)]
                computer_card.append(new_card)
                computer_score = calculate_score(computer_card)
                
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}\n")
            
            print(f"Your final hand: {player_cards}, your final score: {player_score}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
            if computer_score > 21:
                
                print("Computer went over. You win!\n")
            elif computer_score > player_score:
                print("Computer wins!\n")
            elif computer_score < player_score:
                print("You win!\n")
            else:
                print("It's a tie!\n")
            
            replay = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
            if replay == "y":
                clear_terminal()
                print(logo)
                break
            else:
                playing = False
                break

