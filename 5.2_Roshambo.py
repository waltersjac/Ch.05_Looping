'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

win=0
loose=0
rock = 1
paper = 2
scissors = 3
game=1


import random
answer=float(input("Type 1 for rack, 2 for paper, and 3 for scissors"))
number=random.randrange(1,4)
for i in range(1):
    number = random.randrange(1, 4)
    if number == 1:
        print("Rock")
    elif number == 2:
        print("Paper")
    else:
        print("Scissor")
    if answer == number:
        print("Tie")
    elif answer == rock and number == scissors:
        win += 1
        print("win")
    elif answer == paper and number == rock:
        win += 1
        print("win")
    elif answer == scissors and number == paper:
        win += 1
        print("win")
    else:
        loose += 1
        print("loose")
    done = False
    grit = 0
    while not done:
        quit=input("Do you want to Quit?")
        if quit == "y":
            done = True
            game -= 1
        else:
            grit+=1
    print("You didn't quite", grit, "times")



