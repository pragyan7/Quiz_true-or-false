class QuizBrain:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
    
  # ASK THE QUESTIONS TO THE USER
  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)
    
  # CHECK IF WE HAVE REACHED THE END OF THE QUIZ
  def still_has_questions(self):
    return self.question_number < len(self.question_list)
    
  # CHECK IF THE ANSWERS ARE CORRECT
  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("---------------------------\nYou got it right! 😃")
    else:
      print("---------------------------\nYou've got it wrong! 😭")
    # CORRECT ANSWER WILL SHOW AFTER IF/ELSE BLOCK IS COMPLETE
    print(f"The correct answer is {correct_answer}")
    print(f"Your current score is: {self.score}/{self.question_number}\n---------------------------\n")
