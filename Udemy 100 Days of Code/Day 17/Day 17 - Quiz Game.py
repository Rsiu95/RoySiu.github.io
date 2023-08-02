from quiz_master import QuizMaster
from question_model import Questions
from data import question_data

question_bank = []
#questions = Questions()
for info in question_data:
    question_bank.append(Questions(info['text'],info['answer']))
    
#print(question_bank)

quiz_master = QuizMaster(question_bank)

quiz_master.end_of_quiz()

while quiz_master.end_of_quiz():
    quiz_master.ask_question()

score = quiz_master.score
question_number = quiz_master.question_number

print("You've completed the quiz!")
print(f"Your final score was: {score}/{question_number}")