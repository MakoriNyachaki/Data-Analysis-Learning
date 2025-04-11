# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:47:37 2024

@author: The_Makoris
"""
##
# This module defines a class that models exam questions
# A question with a text and an answer.
#

class Question:
    # Constructs a question with empty question and answer
    def __init__(self):
        self._text = ""
        self._answer = ""
        
    # Sets the question text
    # @param questionText the text of this question
    def setText(self, questionText):
        self._text = questionText
    
    # Sets the answer for this question
    # @param correctResponse the answer
    def setAnswer(self, correctResponse):
        self._answer = correctResponse
    
    # Checks a given response for correctness
    # @param response the response to check
    # @return True if the response was correct and False otherwise
    def checkAnswer(self, response):
        return(response == self._answer)
    
    # Display these questions
    def display(self):
        print(self._text)