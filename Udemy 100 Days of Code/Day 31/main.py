from tkinter import *
import pandas
from random import choice
count = 5
# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARDBACK_COLOR = "#91c2af"
file_path = "./Udemy 100 Days of Code/Day 31/"
data_path = "./Udemy 100 Days of Code/Day 31/data/french_words.csv"
images_path = "./Udemy 100 Days of Code/Day 31/images/"

# Retrieve Data
data = pandas.read_csv(data_path)

words = {row.French:row.English for (_, row) in data.iterrows()}
chosen_word = choice(list(words.items()))
#print(len(words))

#remove_word = words.pop(chosen_word[0])

known_words = {}
# Store Known Words (Tick) > get new card
def get_next_card(word):
    words.pop(word[0])
    global new_word 
    new_word = choice(list(words.items()))
    swap_card_back(chosen_word)
    

# get new card > recycle that card
def swap_to_card_back():
    pass

# Countdown timer
def countdown(count):
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
        print(count)
    else:
        swap_card_front(chosen_word)

# swap between card_front.png and card_back.png  
def swap_card_front(word):
    card_front.grid(row = 0, column = 0, columnspan = 3)
    french_label.config(background = "white", text = word[0])
    card_back.grid_forget()

def swap_card_back(word):
    card_back.grid(row = 0, column = 0, columnspan = 3)
    french_label.config(background = CARDBACK_COLOR, text = word[1])
    card_front.grid_forget()

    
# ------------ Create UI ------------ #

# main window
window = Tk()
window.title("Flashy")
window.config(padx = 20, pady = 20, bg = BACKGROUND_COLOR)

# card front
card_front = Canvas(width = 800, height = 550, background = BACKGROUND_COLOR, highlightthickness = 0)
card_front_image = PhotoImage(file = images_path + "card_front.png")
card_front.create_image(400, 290, image = card_front_image)
card_front_text = card_front.create_text(400, 200, text = "French", fill = "black", font = ("Arial", 24, "italic"))
    

# card back
card_back = Canvas(width = 800, height = 550, background = BACKGROUND_COLOR, highlightthickness = 0)
card_back_image = PhotoImage(file = images_path + "card_back.png")
card_back.create_image(400, 290, image = card_back_image)
card_back_text = card_back.create_text(400, 200, text = "English", fill = "black", font = ("Arial", 24, "italic"))
card_back.grid(row = 0, column = 0, columnspan = 3)
 

# Language Labels
french_label = Label(text = chosen_word[1], font = ("Arial", 26, "bold"), background = CARDBACK_COLOR, highlightthickness = 0)
french_label.grid(column = 1, row = 0)


# Tick Button
tick_image = PhotoImage(file = images_path + "right.png")
tick_button = Button(image = tick_image, highlightthickness = 0, borderwidth = 0, command = swap_card_front(chosen_word))
tick_button.grid(row = 1, column = 2)

# X button
x_image = PhotoImage(file = images_path + "wrong.png")
x_button = Button(image = x_image, highlightthickness = 0, borderwidth = 0, command = swap_card_back(chosen_word))
x_button.grid(row = 1, column = 0)

countdown(count)
window.mainloop()