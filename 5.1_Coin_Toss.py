'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
Heads=0
Tails=1
i=2
e=50


while e>0:
    e-=1
    import random
    number=random.randrange(0,2)
    if i in range(50):
        number=random.randrange(0,2)
        print(number)






