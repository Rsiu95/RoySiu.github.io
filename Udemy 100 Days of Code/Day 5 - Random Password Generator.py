import random
import string

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_digits = int(input("How many numbers would you like?\n"))

password_len = num_digits + num_letters + num_symbols

digits = ""
for digit in range(num_digits):
    digits += str(random.randint(0,9))

characters = ""
for digit in range(num_letters):
    characters += random.choice(string.ascii_letters)

symbols = ""
for symbol in range(num_symbols):
    symbols += random.choice(string.punctuation)

password = digits + characters + symbols

print("Your password is:", ''.join(random.sample(password,password_len)))