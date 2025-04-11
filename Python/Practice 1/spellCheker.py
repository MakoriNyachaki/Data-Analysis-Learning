# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 05:16:44 2024

@author: The_Makoris

This program checks which wordsin a file are not present
in a list of correctly spelt words
"""

# Import thr split function from the regular expression module

from re import split


def main():
    # Read the word list and the document
    correctlyspeltWords = readwords("words")
    documentWords = readwords("alice10.txt")
    
    # Print all words that are in the document but not the word list
    
    misspellings = documentWords.difference(correctlyspeltWords)
    for word in sorted(misspellings):
        print(word)

##
# Read all words from a file
# @param filename the name of the file
# @return a set with all lowercased words in the file,
# Here a word is a sequence of upper and lowercase letters
#

def readwords(filename):
    wordSet = set()
    inputFile = open(filename, 'r')
    
    for line in inputFile:
        line = line.strip()
        
        # Use any character other than a-z or A-Z as word delimiters
        parts = split("[^a-zA-Z]+", line)
        for word in parts:
            if len(word) > 0:
                wordSet.add(word.lower())
                
    inputFile.close()
    return(wordSet)

# Start the program
main()

