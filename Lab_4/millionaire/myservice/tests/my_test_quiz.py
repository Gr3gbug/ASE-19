import unittest
import json
from .quiz import Answer, Question 

class TestQuiz(unittest.TestCase):
    
    def test1(self):
        answer1 = Answer("answer1", True)
        answer2 = Answer("answer2", False)
        
        question = Question("test?", [answer1, answer2])
        
        expected = question.checkAnswer("answer1")
        self.assertEqual(expected, True)
        