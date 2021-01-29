from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in question_data:
    text = index["question"]
    answer = index["correct_answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

