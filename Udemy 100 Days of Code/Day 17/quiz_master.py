class QuizMaster:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def ask_question(self):
        #while self.question_number < (len(self.question_list) - 1):
        
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{(self.question_number)}: {question.text} (True/False): ")
        self.check_answer(user_input, question.answer)
        
    
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    
    def end_of_quiz(self):
        return self.question_number < len(self.question_list)