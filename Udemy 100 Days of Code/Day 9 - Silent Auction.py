import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# function to clear terminal
def clear_terminal():
    os.system("cls")
    
print(logo + "\n")
print("Welcome to the secret auction program.\n")

# function to return the max bidder using the "get" function
def return_max_bid(bidding_info):
    max_bid_name = max(bidding_info, key = bidding_info.get)
    return max_bid_name

bidding_directory = {}
bidding_open = True
while bidding_open:
    
    # get user info
    name = input("What is your name?: ")
    user_bid = int(input("What's your bid?: $"))
    bidding_open = False
    
    # add user info into the dictionary
    bidding_directory[name] = user_bid
    
    # check if there are more bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    other_bidders.lower()
    # if so, clear the terminal
    if other_bidders == "yes":
        clear_terminal()
        
    # if it's anything else, exit    
    elif other_bidders != "yes":
        max_bid = return_max_bid(bidding_directory)
        print(f"The winner is {max_bid} with a bid of ${bidding_directory[max_bid]}")
        bidding_open = False