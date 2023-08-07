import turtle

import pandas
file_path = "C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/US-State-Quiz/"
data = pandas.read_csv(file_path + "50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = file_path + "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_guess = 0
total_states = len(data["state"])

data_x = data[data.state == "Arizona"]
# print("a", data_x.x, data_x.y)
# print(type(data_x.x), type(data_x.y))

def create_score_tag(state):
    if state in data["state"].tolist():
        state_turtle = turtle.Turtle()
        state_turtle.ht()
        state_turtle.penup()
        state_coords = data[data.state == state]
        state_x = int(state_coords.x.values[0])
        state_y = int(state_coords.y.values[0])
        state_turtle.goto(state_x, state_y)
        state_turtle.write(state)


def write_final_score(final_score):
    final_score = turtle.Turtle()
    final_score.ht()
    final_score.goto(0,0)
    final_score.write(f"Final Score: {correct_guess}/{total_states}", align = "center", font = ("Courier", 48, "normal"))
    
guessed_states = []        
playing = total_states

while playing:
    user_input = screen.textinput(f"{correct_guess}/{total_states} States Correct","What's another state name?").lower()
    
    if user_input == "exit":
        missing_states = []
        for state in data["state"].tolist():
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv(file_path + "states_to_learn.csv")
        break
    
    for state in data["state"]:
        if user_input == state.lower():
            guessed_states.append(user_input)
            correct_guess += 1
            create_score_tag(state)
        else:
            continue
    # print(guessed_states)
    playing -= 1
    
write_final_score(correct_guess)

screen.exitonclick()

# answer_key = []
# for guess in guessed_states:
#     for state in data["state"].tolist():
#         if guess == state:
#             answer_key.append("correct")
#         else:
#             answer_key.append("incorrect")

# states_to_learn  = {
#     'State': data["state"].tolist(),
#     'Answer': answer_key
# }

# export_data = pandas.DataFrame(states_to_learn)
# export_data.to_csv(file_path + "50_states.csv")
