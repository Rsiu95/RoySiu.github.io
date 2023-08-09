import pandas

file_path = "./Udemy 100 Days of Code/Day 26/"
phonetic_data = pandas.read_csv(file_path + "nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (_, row) in phonetic_data.iterrows()}

converting = True

while converting:
    user_input = input("Enter a word: ").upper()
    
    if user_input == "EXIT":
        break
    
    else:
        converted_list = [phonetic_dict[c] for c in user_input]
        print(converted_list)
        
        new_input = input("Would you like to convert another word? Y/N: ").upper()
        if new_input == "N" or new_input == "EXIT":
            converting = False
            break
        elif new_input == "Y":
            continue
        else:
            print ("Invalid Input.")
            converting = False
            break
