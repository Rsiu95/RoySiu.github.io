morse_code_dict = {
    'A':".-",
    'B':"-...",
    'C':"-.-.",
    'D':"-..",
    'E':".",
    'F':"..-.",
    'G':"--.",
    'H':"....",
    'I':"..",
    'J':".---",
    'K':"-.-",
    'L':".-..",
    'M':"--",
    'N':"-.",
    'O':"---",
    'P':".--.",
    'Q':"--.-",
    'R':".-.",
    'S':"...",
    'T':"-",
    'U':"..-",
    'V':"...-",
    'W':".--",
    'X':"-..-",
    'Y':"-.--",
    'Z':"--..",
    '1':".----",
    '2':"..---",
    '3':"...--",
    '4':"....-",
    '5':".....",
    '6':"-....",
    '7':"--...",
    '8':"---..",
    '9':"----.",
    '0':"-----",
}

start_converting = input("Would you like to convert a some text? (Y/N)\n").upper()
if start_converting == "Y":
    converting = True
else:
    print("Please input either Y or N.")
    exit()

while converting:
    user_input = input("Please type a some text:\n").upper()

    res = []
    for c in user_input:
        if c == ' ':
            continue
        else:
           res.append(morse_code_dict[c]) 
    print(" ".join(res))
    
    continue_input = input("Would you like to convert another? (Y/N)\n").upper()
    if continue_input == "Y":
        continue
    elif continue_input == "N":
        converting = False
        print('Thank you for using Morse-to-Text Converter!')
        break
    else:
        print("Invalid input. Please type either Y/N.")
        converting = False
        break
