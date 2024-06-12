from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

print(logo)
question_bank = []

for i in range(len(question_data)):
  question_data[i] = Question(question_data[i]["text"], question_data[i]["answer"])
  question_bank.append(question_data[i])
  
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()


print(f"\nYou have completed the quiz.\nYour score is: {quiz.score}/{quiz.question_number}")
