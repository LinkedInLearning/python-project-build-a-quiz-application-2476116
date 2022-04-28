# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz


class Question:
    def __init__(self):
        # TODO: define the Question fields
        pass


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    # TODO: define the ask method
    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            # TODO: Check to see if no response was entered

            # TODO: Check to see if either T or F was given

            # TODO: mark this question as correct if answered correctly

            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        # TODO: define the answers for this question

    # TODO: define the ask method
    def ask(self):
        while (True):
            # TODO: Present the question and possible answers

            response = input("? ")

            # TODO: Check to see if no response was entered

            # TODO: mark this question as correct if answered correctly

            break


class Answer:
    def __init__(self):
        pass
        # TODO: define the Answer fields


# if __name__ == "__main__":
#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     q1.ask()
#     q2 = QuestioncMC()
#     q2.text = "What is 2+2?"
#     q2.points = 10
#     q2.correct_answer = "b"
#     ans = Answer()
#     ans.name = "a"
#     ans.text = "3"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "b"
#     ans.text = "4"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "c"
#     ans.text = "5"
#     q2.answers.append(ans)
#     q2.ask()

#     print(q1.is_correct)
#     print(q2.is_correct)
