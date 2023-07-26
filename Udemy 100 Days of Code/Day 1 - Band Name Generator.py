# Simple Print Statement Generator

def BandNameGenerator():
    # Intro print
    print("Welcome to the Band Name Generator.")
    
    # request input from user using the built-in input function
    name = input("What's the name of the city you grew up in?\n")
    location = input("What's your pet's name?\n")
    
    # returns the inputs
    return print("Your band name could be", location, name)

BandNameGenerator()