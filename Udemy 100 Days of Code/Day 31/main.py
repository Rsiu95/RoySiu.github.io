from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

file_path = "./Udemy 100 Days of Code/Day 31/"
data_path = "./Udemy 100 Days of Code/Day 31/data/french_words.csv"
images_path = "./Udemy 100 Days of Code/Day 31/images/"

current_card = {}
to_learn = {}

try:
    
    # Try to see if there's a file for words to learn
    data = pandas.read_csv(file_path + "data/words_to_learn.csv")
except FileNotFoundError:
    
    # Open the original data file if not found
    original_data = pandas.read_csv(file_path + "data/french_words.csv")
    print(original_data)
    
    # extract data
    to_learn = original_data.to_dict(orient="records")
else:
    # extract data
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    
    # cancel timer to reset on next card
    window.after_cancel(flip_timer)
    
    # select a random card
    current_card = random.choice(to_learn)
    
    # set canvas title, and word to be shown
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    
    # flip the current card after 3000ms
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    
    # flip you card by changing canvas config
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    # remove the current card from dict
    to_learn.remove(current_card)
    print(len(to_learn))
    
    # add it into new csv called to learn
    data = pandas.DataFrame(to_learn)
    data.to_csv(data_path + "words_to_learn.csv", index = False)
    
    # next card
    next_card()

# ------------ Create UI ------------ #

# main window
window = Tk()
window.title("Flashy")
window.config(padx = 20, pady = 20, bg = BACKGROUND_COLOR)

# set timer
flip_timer = window.after(3000, func = flip_card)

# Create main canvas
canvas = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file = images_path + "card_front.png")
card_back_image = PhotoImage(file = images_path + "card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)

# Tick Button
tick_image = PhotoImage(file = images_path + "right.png")
tick_button = Button(image = tick_image, highlightthickness = 0, borderwidth = 0, command = next_card)
tick_button.grid(row = 1, column = 1)

# X button
x_image = PhotoImage(file = images_path + "wrong.png")
x_button = Button(image = x_image, highlightthickness = 0, borderwidth = 0, command = is_known)
x_button.grid(row = 1, column = 0)

# start with next card
next_card()
window.mainloop()