class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        # print(self.question_list[0].text)

    def still_has_question(self):
        return self.question_number < len(self.question_list) # 리턴 값으로 바로 참 / 거짓을 반환

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        result = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(result, current_question.answer)

    def check_answer(self, result, correct_answer):
        if result.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
