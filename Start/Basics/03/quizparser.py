# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizParser builds a quiz from a source file
import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):
    """
    The QuizParser class loads a particular quiz file, parses it, and returns
    a fully-built Quiz object that can then be presented to the user.
    """

    def __init__(self):
        self.new_quiz = Quiz()
        #TODO: properties for the parser state and current question and answer

    def parse_quiz(self, quizpath):
        # load the file contents
        quiztext = ""
        with open(quizpath, "r") as quizfile:
            if quizfile.mode == "r":
                quiztext = quizfile.read()

        #TODO: parse the file

        # return the finished quiz
        return self.new_quiz

    def startElement(self, tagname, attrs):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.PARSE_QUIZ
            self.new_quiz.name = attrs["name"]
        #TODO: process the rest of the tags

    def endElement(self, tagname):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.IDLE
        #TODO: process the rest of the tags

    def characters(self, chars):
        #TODO: process the text content
        pass


if __name__ == "__main__":
    app = QuizParser()
    qz = app.parse_quiz("Quizzes/SampleQuiz.xml")
    print(qz.name)
    print(qz.description)
    print(len(qz.questions))
    print(qz.total_points)
    for q in qz.questions:
        print(q.text)
