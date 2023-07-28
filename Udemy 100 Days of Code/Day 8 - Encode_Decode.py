
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

def get_user_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return [direction, text, shift]

# def encode_message(message, encryption):
#     message = user_input[1]
#     encrypted_message = []
#     for c in message:
#         encrypted_char = ord(c) + encryption
#         encrypted_message.append(chr(encrypted_char))
#     return "".join(encrypted_message)  + "\n"

# def decode_message(message, decryption):
#     message = user_input[1]
#     decrypted_message = []
#     for c in message:
#         decrypted_char = ord(c) - decryption
#         decrypted_message.append(chr(decrypted_char))
#     return "".join(decrypted_message) + "\n"

def caeser(direction, message, shift):
    new_message = []
    if direction == "decode":
        shift *= -1
    for c in message:
        new_char = ord(c) + shift
        new_message.append(chr(new_char))
    new_message = "".join(new_message)
    output = print(f"Here's the {direction}d result: {new_message}\n")
    return output

while True:
    user_input = get_user_input()
    caeser(user_input[0], user_input[1], user_input[2])
    # if user_input[0] == "encode":
    #     print("Here's the encoded result:",encode_message(user_input[1], user_input[2]))
    # elif user_input[0] == "decode":
    #     print("Here's the decoded result:", decode_message(user_input[1], user_input[2]))
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if repeat == "no":
        break
