  #Sign your name: Jacob Walters

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x
print("The total is:", total)

  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(2,102,2):
    print(i)


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i=10

while i>-1:
    print(i)
    i -= 1
print("Blast off")


'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
my_number=random.randrange(1,11)
for i in range(5):
    my_number = random.randrange(1,11)
    print(my_number)



'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
total=0
Positive_Count=0
Zero_Count=0
Negative_Count=0

for i in range (7):
    given_number = float(input("Give me a number!"))
    total+=given_number
    if given_number>0:
        Positive_Count+=1
    elif given_number==1:
        Zero_Count+=1
    else:
        Negative_Count+=1

print(total)
print("Positives",Positive_Count,"Zeros",Zero_Count,"Negatives",Negative_Count)