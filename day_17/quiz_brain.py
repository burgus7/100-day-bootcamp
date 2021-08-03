class QuizBrain():
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        guess = input(f"Q.{self.q_number}: {current_question.text} (True/False)?: ")
        self.check_answer(guess, current_question.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, guess, correct):
        if guess.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.q_number}.")
        print('\n')
