# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:38:46 2019

@author: richardg71
"""


def getMonth():
    month = 0
    while (month < 1 or month > 12):
        month = int(input("Enter a month(1/12): "))
        if (month < 1 or month > 12):
            print("Please enter a month between 1 and 12")
    return month

def display(daysInMonth, startDay):
    for i in range(startDay):
        print("    ", end = '')
    for i in range(1, daysInMonth + 1):
        print('{:>4}'.format(i), end = '')
        if ((i + startDay) % 7 == 0):
            print('')
        
    
month = getMonth()
daysInMonth = 31
startDay = 3
display(daysInMonth, startDay)

