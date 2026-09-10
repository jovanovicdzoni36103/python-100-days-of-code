class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.quiz_name = "Python Beginner Quiz"

    def has_more_questions(self):
        return self.current_question < len(self.questions)

    def next_question(self):
        print(f"\nQuestion {self.current_question + 1}")

        current_question = self.questions[self.current_question]

        print(current_question.text)
        answer = input("Your answer: ").lower()

        if answer == current_question.answer.lower():
            self.score += 1
            self.current_question += 1
            return "Correct!", True
        else:
            correct_answer = current_question.answer
            self.current_question += 1
            return f"Incorrect! The correct answer was: {correct_answer}", False