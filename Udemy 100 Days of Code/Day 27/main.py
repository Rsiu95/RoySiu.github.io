from tkinter import *

# from videos
# window = Tk()
# window.title("Day 26 - GUI")
# window.minsize(width = 500, height = 300)
# window.config(padx = 20, pady = 20)

# # Label
# my_label = Label(text = "I am a label", font = ("Arial", 24, "bold"))
# my_label.grid(column = 2, row = 3)


# my_label.config(text = "New Text")

# def button_clicked():
#     my_label["text"] = get_string()
    

# # Button
# button = Button(text = "Click ME", command = button_clicked)
# button.grid(column = 1, row = 1)

# new_button = Button(text = "I'm another button", command = button_clicked)
# new_button.grid(column = 2, row = 0)

# def get_string():
#     return user_input.get()    

# # Entry
# user_input = Entry(width = 10)
# user_input.grid(column = 3, row = 3)

# window.mainloop()

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)
window.config(padx = 20, pady = 20)

# Miles Label
miles_label = Label(text = "Miles", font = ("Arial", 16))
miles_label.grid(column = 2, row = 0)

# equals label
equals_label = Label(text = "is equal to", font = ("Arial", 16))
equals_label.grid(column = 0, row = 1)

# km label
miles_label = Label(text = "Km", font = ("Arial", 16))
miles_label.grid(column = 2, row = 1)

# converted value label
converted_value = Label(text = "0", font = ("Arial", 16))
converted_value.grid(column = 1, row = 1)

def convert_input():
    input = float(user_input.get())
    converted_input = round(input * 1.609344, 2)
    converted_value["text"] = converted_input
    
# Button 
calculate_button = Button(text = "Calculate", command = convert_input)
calculate_button.grid(column = 1, row = 2)

# user entry field
user_input = Entry(width = 10)
user_input.grid(column = 1, row = 0)

window.mainloop()