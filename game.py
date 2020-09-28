# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:32:07 2019

@author: richardg71
"""
"""
Course: CS101
File: Game
Project: project04
Author: Mac Allen
Description:
 <What does your project/program do?>
"""
"""
Instructions:
 Here's your chance to be creative. Write a program that will allow the user
 to play a "Choose Your Own Adventure" type game. Here are the requirements
 of complexity:
 1) Each decision must have only 2 choices to choose from.
 Use "1" and "2" as your options (to make grading simpler.)
 2) The game must have the user make at least 3 choices before the game ends.
 3) Your game must have only two possible endings
 (ie. Live/Die, Win/Lose, Escaped/Captured).
 4) The code for the ending situations must be more than just a single print
 statement that says "You WIN!" but should be more exciting!
 (ie. This is better:

 *******************************************
 * *
 * You are the best in the land! *
 * *
 *******************************************
 )
 5) For full credit (you can get 90% without it), call functions as a result
 of making a choice.
 (ie.
 if choice1 == "1":
 openRedDoor()
 elif choice1 == "2":
 runOtherWay()
 6) For extra credit (5-10%), learn to use a library to do something special,
 like display a graphic or tell the user how much time they took to finish.

 For an example of how to create this type of game, watch this video:
 https://www.youtube.com/watch?v=DEcFCn2ubSg

"""
# TODO -> Add your project code here
#functions
def openingChoice() :
 openingOptions = ['yes', 'no']
 choice1 = ''
 while choice1 not in openingOptions :
     print('Welcome to the Adventure of Life!')
     print('You have just graduated high school.')
     print('It is time for your next adventure!')

 choice1 = input('Would you like to go to college immediately? (yes/no) ')
 if choice1 == openingOptions[0] : #yes
     college()
 elif choice1 == openingOptions[1] : #no
     nocollege()
 return
def college() :
 print("This is going to be adventure, I hope you're ready!")
 choice1aOptions = ['1', '2']
 choice2 = ''
 while choice2 not in choice1aOptions :
     choice2 = input('Will you go to a community college (1) or a 4-year university (2)? ')
 if choice2 == choice1aOptions[0] : #comminity college
     communityCollege()
 elif choice2 == choice1aOptions[1] :
     university()
 return
def communityCollege() :
 print('You are going to save a ton of money!')
 choice2aOptions = ['1', '2']
 choice3 = ''
 while choice3 not in choice2aOptions :
     choice3 = input("""You have two options:
(1) Live at home
(2) Get your own apartment
What will you do? """)
 if choice3 == choice2aOptions[0] :
     winning()
 elif choice3 == choice2aOptions[1] :
     winning()
 return
def university() :
 print('You are ambitious!')
 choice2bOptions = ['1', '2']
 choice3 = ''
 while choice3 not in choice2bOptions :
     choice3 = input("""We all know that there are truly only two options
for college. And you have to choose one of them.
(1) BYU-Idaho (a.k.a. the best university)
(2) another state school
What is your choice? """)
 if choice3 == choice2bOptions[0] :
     winning()
 elif choice3 == choice2bOptions[1] :
     losing()
 return
def nocollege() :
 print("You dont care what people think, you're gonna make it big!")
 choice1bOptions = ['1', '2']
 choice2 = ''
 while choice2 not in choice1bOptions :
     choice2 = input("""There are many routes you can take, but lets say
you can only make one of these two.
(1) Join the military
(2) Get a job as a civilian
Which would you choose? """)
 if choice2 == choice1bOptions[0] :
     military()
 elif choice2 == choice1bOptions[1] :
     civilian()
 return
def military() :
 print("I'm glad you chose to serve the U.S.A.!")
 choice2cOptions = ['1', '2']
 choice3 = ''
 while choice3 not in choice2cOptions :
 choice3 = input("""Now that you are in the military there are a myriad of
options,
like which branch you will be in or what job you will have.
I am only curious about one thing though.
Will you choose to
(1) Stay in the military for 20 years and retire, or
(2) Get dishonorably discharged.
What is your choice? """)
 if choice3 == choice2cOptions[0] :
 winning()
 elif choice3 == choice2cOptions[1] :
 losing()
 return
def civilian() :
 print("There's nothing better than manking money besides making more money.")
 choice2dOptions = ['1', '2']
 choice3 = ''
 while choice3 not in choice2dOptions :
 choice3 = input("""Some people don't need college if they make the right
decisions.
Obviosly you know that. It's time for you to make the right
decision. If you only had the option of these two which would you choose?
(1) Work at discount tire and move up the ranks, or
(2) Work at a grocery store and never get promoted.
Which route will you take? """)
 if choice3 == choice2dOptions[0] :
 winning()
 elif choice3 == choice2dOptions[1] :
 losing()
 return
def winning() :
 print('{:#^42}'.format(''))
 print('#{: ^40}#'.format('You have won the game of life!'))
 print('{:#^42}'.format(''))
 winnerOptions = ['yes', 'no']
 playAgain = ''
 while playAgain not in winnerOptions :
 playAgain = input('Would you like to play again? (yes/no) ')
 if playAgain == winnerOptions[0] :
 openingChoice()
 elif playAgain == winnerOptions[1] :
 print('Thank you for playing.')
 return
def losing() :
 print('{:#^42}'.format(''))
 print('#{: ^40}#'.format('You have lost at life!'))
 print('#{: ^40}#'.format('Better luck next time...'))
 print('{:#^42}'.format(''))
 loserOptions = ['yes', 'no']
 playAgain = ''
 while playAgain not in loserOptions :
 playAgain = input('Would you like to try to win again? (yes/no) ')
 if playAgain == loserOptions[0] :
 openingChoice()
 elif playAgain == loserOptions[1] :
 print('You are eternally a loser!')
 return
#main code
openingChoice()
