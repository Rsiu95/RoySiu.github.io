from tkinter import *
from tkinter import messagebox
from random import randrange
import json
import pyperclip

#----------------------------- CONSTANTS -----------------------------#
file_path = "./Udemy 100 Days of Code/Day 30/"
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
    
    new_data = {
        website_name: {
            "username": username,
            "password": password,
        }
    }
    
    if website_name == "" or username == "" or password == "":
        messagebox.showerror('Error', 'Please fill all the fields!')
        
    else:
        if len(website_name) == 0 or len(password) == 0:
            messagebox.showinfo(title = "Oops", message = "Please make sure you haven't left any fields empty.")
        else:
            try:
                with open((file_path + 'user_login_details.json'), mode='r') as file:
                    
                    # read old data
                    data = json.load(file)
                    
            except FileNotFoundError:
                with open(file_path + "user_login_details.json", mode = 'w') as file:
                    json.dump(new_data, file, indent = 4)
            else:
                # update data
                data.update(new_data)
    
                with open((file_path + 'user_login_details.json'), mode='w') as file:    
                    # save updated data
                    json.dump(data, file, indent = 4)
            
            finally:    
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------- SEARCH PASSWORDS ---------------------- #
def search_user_info():
    with open(file_path + 'user_login_details.json', mode = 'r') as user_info:
        data = json.load(user_info)
        try: 
            website_name = website_entry.get()
            username = data[website_name]["username"]
            password = data[website_name]["password"]
            messagebox.showinfo(title = f"{website_name}", message = f"Username: {username}\nPassword: {password}")
        except:
            messagebox.showerror(title = "Error", message = "No Data File Found.")

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
website_entry = Entry(width = 35, bg = "white", highlightthickness = 1, highlightcolor = "white")
website_entry.grid(column = 1, row = 1)

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

# Search Button:
search_button = Button(text = "Search", width = 10, command = search_user_info)
search_button.grid(column = 2, row = 1)

# Mainloop
window.mainloop()
