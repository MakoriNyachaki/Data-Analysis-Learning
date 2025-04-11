# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:42:01 2024

@author: The_Makoris
"""
# @TOTAL_PERCENTAGE marked out of 100%

TOTAL_PERCENTAGE = 100.0


##
# makeList function creates a list of float numbers
# @list_len: length of the list
# @return grades return the list of float numbers
#

def makeList(list_len):
    grades = []
    for grade in range(list_len):
        grade = float(input("Enter grade: "))
        grades.append(grade)
    return(grades)

##
# sumList function finds the sum of elements in a list
# @sumGrades the list of elements whose sum is to be found
# @return totl returns the sum of list
#

def sumList(sumGrades):
    total = 0
    for grade in sumGrades:
        try:
            if grade >= 0.0 or grade <= 100.0: 
                total += grade
            else:
                print(f'Rejected grades{grade}')
        except Exception:
            print(ValueError)                   
                   
    return(total)

def avgMarks(no_subs, total_mks):
    return(total_mks // no_subs)

##
# awardGrade function calculates the average grade and awards a grade for the average
# @total_mks the total marks scored by a student
#
def awardGrade(average_marks):
    
    try:
        if average_marks > 83 and average_marks <= 100:
            return("A")
        elif average_marks <= 83 and average_marks > 74:
            return("A-")
        elif average_marks <= 74 and average_marks > 66:
            return("B+")
        elif average_marks <= 66 and average_marks > 58:
            return("B")
        elif average_marks <= 58 and average_marks > 51:
            return("B-")
        elif average_marks <= 51 and average_marks > 44:
            return("C+")
        elif average_marks <= 44 and average_marks > 37:
            return("C")
        elif average_marks <= 37 and average_marks > 30:
            return("C-")
        elif average_marks <= 30 and average_marks > 24:
            return("D+")
        elif average_marks <= 24 and average_marks > 19:
            return("D")
        elif average_marks <= 19 and average_marks > 15:
            return("D-")
        elif average_marks <= 15 and average_marks >= 0:
            return("E")
        else:
            return("F")
    except Exception:
        return(ValueError)
    
def gradesAwardSubjects(scores):
    yourGrades = []
    for score in scores:
        print(score)
        if score > 83 and score <= 100:
            return("A")
        elif score <= 83 and score > 74:
            return("A-")
        elif score <= 74 and score > 66:
            return("B+")
        elif score <= 66 and score > 58:
            return("B")
        elif score <= 58 and score > 51:
            return("B-")
        elif score <= 51 and score > 44:
            return("C+")
        elif score <= 44 and score > 37:
            return("C")
        elif score <= 37 and score > 30:
            return("C-")
        elif score <= 30 and score > 24:
            return("D+")
        elif score <= 24 and score > 19:
            return("D")
        elif score <= 19 and score > 15:
            return("D-")
        elif score <= 15 and score >= 0:
            return("E")
        else:
            return("F")
        
    yourGrades.append(score)
    return(yourGrades)
        
        
        
        

    

##
# main functions does all the logistics in the functions

def main():
    listLen = int(input("Enter the length  of your list: "))
    grades = makeList(listLen)
    print(f"\n{grades}\n")
    add = sumList(grades)
    print(gradesAwardSubjects(grades))
    print(f'\n\n\t\t\t\tYou Score\n\n{50 * "="}\n\nGrade: {awardGrade(avgMarks(listLen, add))} \tPoints: {avgMarks(listLen, add)} ')
    # print(f'\nThe list has {listLen} elements:{grades} \nTotal: {add}')

main()