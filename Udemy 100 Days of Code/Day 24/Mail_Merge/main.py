with open("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 24/Mail_Merge/Names/invited_names.txt") as names:
    invited_names = []
    for name in names.readlines():
        
        invited_names.append(name.strip('\n'))

with open("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 24/Mail_Merge/starting_letter.txt") as letter:
    updated_letter = letter.read()

for name in invited_names:
    
    with open("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 24/Mail_Merge/ReadyToSend/" + name +".txt", mode = "w") as ready:
        ready.write(updated_letter.replace("[name]", name))
