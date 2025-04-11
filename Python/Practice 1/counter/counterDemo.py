# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:14:06 2024

@author: The_Makoris
"""
##
# This program demonsrates the counter class
#

from Counter import Counter


tally = Counter()

tally.reset()
tally.click()
tally.click()

result = tally.getValue()

print("Value_1:", result)

tally.click()
result = tally.getValue()
print("Value_2:", result)