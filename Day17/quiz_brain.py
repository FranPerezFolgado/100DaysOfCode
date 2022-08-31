class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        pass

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Next question's category {current_question.category},  difficulty {current_question.difficulty}")
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False)?:")
        self.check_answer(user_answer, current_question.correct_answer)
        print("\n")
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right! :D")
            self.score += 1
        else:
            print("That's wrong :(")
        
        print(f"The correct answer was {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")