'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

thirst=0
camel_Tiredness=0
Canteen_Drinks=5
Natives=-20
Distance_Traveled=0
done=False
Oasis=20

print("Welcome to camel game.")
while not done:
    print("A.Drink From Canteen B.Ahead Moderate Speed C.Ahead Full Speed D.Stop for the night E.Status Check Q.Quit")
    print("Natives", Distance_Traveled - Natives, "Miles Behind")
    if Natives >= Distance_Traveled:
        print("The Natives Caught you.")
        print(Distance_Traveled, "Miles Traveled")
        done=True
    elif camel_Tiredness>=8:
        print("Your camel is dead.")
        print(Distance_Traveled, "Miles Traveled")
        done=True
    elif thirst>=6:
        print("You died of thirst.")
        print(Distance_Traveled, "Miles Traveled")
        done=True
    else:
        if Distance_Traveled-Natives<=15:
            print("The Natives are close")
        elif camel_Tiredness>=5:
            print("Your Camel is tired")
        elif thirst>=4:
            print("you are thirsty")
        Action=input("What do you do?")
        if Action.upper()=="A":
            thirst=0
            Canteen_Drinks-=1
        elif Action.upper=="B":
            thirst+=1
            camel_Tiredness+=1
            Distance_Traveled+=random.randrange(7,15)
            print(Distance_Traveled, "Miles Traveled")
            if Oasis==random.randrange(1,21):
                print("You found an oasis!")
                Canteen_Drinks=5
                thirst=0
                camel_Tiredness=0
        elif Action.upper()=="C":
            camel_Tiredness+=random.randrange(1,4)
            Distance_Traveled+=random.randrange(10,21)
            print(Distance_Traveled,"Miles Traveled")
            if Oasis==random.randrange(1,21):
                print("You found an oasis!")
                Canteen_Drinks = 5
                thirst = 0
                camel_Tiredness = 0
        elif Action.upper()=="D":
            camel_Tiredness=0
            print("Your camel is happy.")
        elif Action.upper()=="E":
            print("drinks",Canteen_Drinks,"Miles Traveled",Distance_Traveled,"Camel Tiredness",camel_Tiredness)
        elif Action.upper()=="Q":
            quit=input("Do you want to quit?")
            if quit.upper()=="Y":
                print("Game End")
                done=True
        Natives += random.randrange(7, 15)