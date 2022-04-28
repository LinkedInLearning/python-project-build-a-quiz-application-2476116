# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        #TODO: the most recently selected quiz

        #TODO: initialize the collection of quizzes

        #TODO: stores the results of the most recent quiz

        #TODO: the name of the person taking the quiz


        #TODO: make sure that the quiz folder exists

        #TODO: build the list of quizzes

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        #TODO: parse the XML files in the directory

    #TODO: print a list of the currently installed quizzes
    def list_quizzes(self):
        pass

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        pass

    # prints the results of the most recently taken quiz
    def print_results(self):
        pass

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("Quizzes")
    qm.list_quizzes()
