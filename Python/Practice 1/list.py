# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:43:30 2023

@author: The_Makoris
"""

class List:
    
    def __init__(self):
        self.total
        self.count
        self.avg

    ##
    # listTotal finds the total of the list elements
    # @param values the list input
    # return the total
    #

    @staticmethod
    def listTotal(values):
        total = 0
        for value in values:
            total += value
        return(total)

    ##
    # listAverage finds the average of a list
    # @param values the list input
    # return the average(avg)
    #

    @staticmethod
    def listAverage(values):
        count = 0
        for value in values:
            count += 1

        avg = List.listTotal(values) / count

        return(avg)

    def mode(values):
        pass
        