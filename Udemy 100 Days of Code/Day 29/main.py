from tkinter import *
from tkinter import messagebox
from random import randrange
import pyperclip

#----------------------------- CONSTANTS -----------------------------#
file_path = "./Udemy 100 Days of Code/Day 29/"
FONT = ("Arial", 16)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    random_password = ""
    for _ in range(17):
        random_password += chr(randrange(33, 126))
    password_entry.delete(0, END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_name = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website_name == "" or username == "" or password == "":
        messagebox.showerror('Error', 'Please fill all the fields!')
        
    else:
        is_yes = messagebox.askyesno(f"{website_name} User Login Information", message = f"Are you happy with the following information: \
            \nWebsite: {website_name}\nUsername: {username}\nPassword: {password}")
        
        if is_yes:
            user_data = [website_name, username, password]
            user = (" | ").join(user_data)
            with open((file_path + 'user_login_details.txt'), mode='a') as file:
                file.write(user + "\n")
            
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Main Window
window = Tk()
window.title("Password Manager")
window.config(padx = 30, pady = 50, bg = "white")

# Image Canvas
canvas = Canvas(width = 200, height = 200, bg = "white", highlightthickness = 0)
image_path = PhotoImage(file = (file_path + "logo.png"))
canvas.create_image(100, 100, image = image_path)
canvas.grid(column = 1, row = 0) # probably use .pack() here

# Website Label + Entry
website_text = Label(text = "Website:", font = (FONT), bg = "white", highlightthickness = 0)
website_text.grid(column = 0, row = 1)
website_entry = Entry(width = 45, bg = "white", highlightthickness = 1, highlightcolor = "white")
website_entry.grid(column = 1, row = 1, columnspan = 2)

# # Email/Username Label + Entry
username_text = Label(text = "Email/Username:", font = (FONT), bg = "white", highlightthickness = 0)
username_text.grid(column = 0, row = 2)
username_entry = Entry(width = 45, bg = "white", highlightthickness = 1, highlightcolor = "white")
username_entry.insert(0, "rsiu95@gmail.com")
username_entry.grid(column = 1, row = 2, columnspan = 2)

# Password Label + Entry
password_text = Label(text = "Password:", font = (FONT), bg = "white", highlightthickness = 0)
password_text.grid(column = 0, row = 3)
password_entry = Entry(width = 27, bg = "white", highlightthickness = 1, highlightcolor = "white")
password_entry.grid(column = 1, row = 3)

# Generate Password Button
generate_button = Button(text = "Generate Password", command = generate_password)
generate_button.grid(column = 2, row = 3)

# Add to txt button
add_button = Button(text = "Add", width = 39, command = save_password)
add_button.grid(column = 1, row = 4, columnspan = 2)

# Mainloop
window.mainloop()
