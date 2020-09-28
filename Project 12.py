# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:11:21 2020

@author: richardg71
"""

def addNewStudent(classList):
    studentName = input("What is the student's name: ")
    classList.append(studentName)
    return classList

def displayClassList(classList):
    print("********** Class List **********")
    for i in range(len(classList)):
        print('{:<31}'.format("* " + str(i + 1) + "  " + classList[i]) + "*")
    print("********************************")
    return

def editClassList(classList):
    itemIndex = int(input("Which student do you want to change? "))
    studentName = input("Enter the name of the new student? ")
    classList[itemIndex - 1] = studentName
    return classList

def checkOrRemoveClassList(classList):
    print("Calling checkOrRemoveClassList")
    return classList

def displayMenu():
    print("Menu")
    print("   n - Add a Student")
    print("   d - Display Class List")
    print("   e - Edit Class List")
    print("   c - Check or Remove Student")
    print("   ? - Display this Menu")
    print("   q - Quit this Program")
    return


user_input = 'n'
classList = []
displayMenu()
while(user_input != 'q'):
    user_input = input("> ")
    if (user_input == 'n'):
        classList = addNewStudent(classList)
    elif(user_input == 'd'):
        displayClassList(classList)
    elif(user_input == 'e'):
        classList = editClassList(classList)
    elif(user_input == 'c'):
        classList = checkOrRemoveClassList(classList)
    elif(user_input == '?'):
        displayMenu()
    elif(user_input == 'q'):
        print("Good bye")
    else:
        print("Command not recognized")
    