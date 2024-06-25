from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question) # 객체의 묶음을 표시

# print(question_text)
# print(question_answer)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question(): # if quiz still has question remaining:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}") # quize.question_number 함수 써도 같음.


# open TRIVIA database를 이용해서 사용자 제공의 일반상식 문제 데이터베이스로 무료로 이용할 수 있다.
# 3000개 이상의 검증된 질문을 보유하고 있어서 골라 사용가능하다.