class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number+=1
        self.check_answer(input(f"Q.{self.question_number+1} {current_question.question} (True/False)\n"), current_question.answer)
    
    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("\nYou got it right!\n")
            self.score+=1
        else:
            print("You got it wrong!\n")
        print(f"Correct answer : {current_answer}\n")
        print(f"Your score : {self.score}\n")
