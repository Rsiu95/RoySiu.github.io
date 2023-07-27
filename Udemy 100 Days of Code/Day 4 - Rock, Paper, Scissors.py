from random import randint

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

Rock = "    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n"

Paper = "    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)"

Scissors = "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"

computer_input = [Rock, Paper, Scissors]

if user_input == 0:
    print(Rock)
    print("\nComputer chose:")
    output = computer_input[randint(0,2)]
    if output == Rock:
        print(output)
        print("\nIt's a draw")
    elif output == Paper:
        print(output)
        print("\nYou lose")
    elif output == Scissors:
        print(output)
        print("\nYou win!")

elif user_input == 1:
    print(Paper)
    print("\nComputer chose:")
    output = computer_input[randint(0,2)]
    if output == Rock:
        print(output)
        print("\nYou win!")
    elif output == Paper:
        print(output)
        print("\nIt's a draw")
    elif output == Scissors:
        print(output)
        print("\nYou lose")

elif user_input == 2:
    print(Scissors)
    print("\nComputer chose:")
    output = computer_input[randint(0,2)]
    if output == Rock:
        print(output)
        print("\nYou lose")
    elif output == Paper:
        print(output)
        print("\nYou win!")
    elif output == Scissors:
        print(output)
        print("\nIt's a draw.")

