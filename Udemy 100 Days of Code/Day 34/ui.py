from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
file_path = "./Udemy 100 Days of Code/Day 34/"
image_path = file_path + "images/"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        self.canvas = Canvas(height = 250, width = 300)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width = 280,
            text = "dummy text", 
            font = ("Arial", 20, "italic")
            )
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        # Tick button
        self.tick = PhotoImage(file = image_path + "true.png")
        self.tick_button = Button(image = self.tick, highlightthickness = 0, borderwidth = 0, command = self.answer_true)
        self.tick_button.grid(row = 2, column = 0)

        # X button
        self.x_image = PhotoImage(file = image_path + "false.png")
        self.x_button = Button(image = self.x_image, highlightthickness = 0, borderwidth = 0, command = self.answer_false)
        self.x_button.grid(row = 2, column = 1)
        
        # score_label
        self.label = Label(text = f"Score: 0", bg = THEME_COLOR, fg = "white", font =("Arial", 15))
        self.label.grid(row = 0, column = 1)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You've reached the end of the quiz!\nYour final score was {self.quiz.score}/{self.quiz.question_number}")
            self.x_button.config(state = "disabled")
            self.tick_button.config(state = "disabled")
        
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg = "red")
            
        self.window.after(1000, self.get_next_question)
        
class BankAccount:
    def __init__(self, balance, account_type):
        self.balance = balance
        self.account_type = account_type
        
    def total_balance(self):
        