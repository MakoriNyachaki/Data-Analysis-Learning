# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:55:55 2024

@author: The_Makoris
"""

##
# This program shows a simple quiz with one question
#

from question import Question

# Create the question and expeted answer
q = Question()

q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")

# Display the question and obtain the user's response
q.display()
response = input("Your answer: ")

print(q.checkAnswer(response))