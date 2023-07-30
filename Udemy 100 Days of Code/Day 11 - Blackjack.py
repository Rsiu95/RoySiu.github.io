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

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def convert_card(card):
    if card == "A":
        return 1
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
    return sum(cards)

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
if start_game == "y":
    playing = True
    print(logo)
else:
    playing = False

while playing:
    player_cards = get_cards(cards)
    print(player_cards)
    player_score = 0
    for card in player_cards:
        player_score += convert_card(card)
        
    #player_score = calculate_score(player_cards)
    computer_card = cards[random.randint(0,12)]
    
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_card}")
    
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == "y":
        player_cards.append(cards[random.randint(0,12)])
        
    
    break
    
#    if start_game != "y":
#        break
    