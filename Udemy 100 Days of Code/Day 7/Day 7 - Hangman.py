from random import randint
import re, os, hangman_art, hangman_words

# function to clear terminal
def clear_terminal():
    os.system("cls")

# Retrieves a random word from hangman_words
word_list = hangman_words.word_list

# Print the starting hangman ASCII art logo
print(hangman_art.logo + "\n")

# Set the game state to False and wait for the Enter key 
# to be pressed before starting the game.
game_start = False
input("\nPress Enter to start!\n")
game_start = True

# Select any random word from the list of words.
word = word_list[randint(0, len(word_list) - 1)]
print(word)
# I opted to split the word into a list to store it and check it against the final guessed solution
split_word = list(" ".join(word))
split_word.append(" ")

# Show how many letters in the word denoted by _.
output = "_ " * len(word)
print(output + "\n")

# Set the lives to 6 as the ASCII hangman has 6 body parts.
lives = 6
# guessed letters
guessed_letters = []
# Main loop
while lives > 0 and game_start == True:
      
    # request user input  
    guess = input("Guess a letter: ").lower()
    
    # update the guessed letters
    guessed_letters.append(guess)
    
    # clears the terminal
    clear_terminal()
    
    # find the index of the guess in the word
    matched_chars = re.finditer(guess, word)
    char_index = [chars.start() for chars in matched_chars]
      
    # store the correct guesses into its own list
    correct_guesses = list(output)


    # check that the guess is correct
    if guess in word and guess not in correct_guesses:
        
        # update the stored correct guesses position with our guess
        for char in char_index:
            correct_guesses[char * 2] = guess
            output = "".join(correct_guesses)
      
        print(hangman_art.stages[lives])
        print("You've guessed " + " ".join(guessed_letters) + "\n")
        print(output + "\n")

        # win check
        if correct_guesses == split_word:
            print("You win!")
            game_start = False
      
      # check for letters that had already been guessed
    elif guess in correct_guesses:
        print(hangman_art.stages[lives])
        output = "".join(correct_guesses)
        print("You've guessed " + " ".join(guessed_letters))        
        print(output + "\n")
        print(f"You've already guessed the letter {guess}.\n")
      

    else:
        # Handles game over
        if lives == 1:
            print(hangman_art.stages[0])
            print(f"You lose! The correct word was {word}")
            game_start = False
            
        # reduce the lives by 1               
        else:
            lives -= 1
            print(hangman_art.stages[lives])
            print("\nYou've guessed " + " ".join(guessed_letters) + "\n")
            print("\n" + output)
            
            print(f"\nYou guessed {guess}, that's not in the word. You lose a life.\n")
