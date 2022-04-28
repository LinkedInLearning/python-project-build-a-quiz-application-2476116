# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# The Quiz and Question classes define a particular quiz
import datetime
import sys

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0

    def print_header(self):
        print("\n\n*******************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*******************************************\n")

    def print_results(self, quiztaker, thefile=sys.stdout):
        print("*******************************************",
              file=thefile, flush=True)
        print(f"RESULTS for {quiztaker}", file=thefile, flush=True)
        print(f"Date: {datetime.datetime.today()}", file=thefile, flush=True)
        print(
            f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile, flush=True)
        print(f"SCORE: {self.score} points of possible {self.total_points}",
              file=thefile, flush=True)
        print("*******************************************\n",
              file=thefile, flush=True)

    def take_quiz(self):
        # initialize the quiz state
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False

        # print the header
        self.print_header()

        # execute each question and record the result
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points
            print("------------------------------------------------\n")

        # return the results
        return (self.score, self.correct_count, self.total_points)


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while (True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if (response[0] != "t" and response[0] != "f"):
                print("Sorry, that's not a valid response. Please try again")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")

            response = input("? ")

            if (len(response) == 0):
                print("Sorry, that's not a valid response. Please try again")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break


class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
