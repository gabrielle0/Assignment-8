#Steps:
#Step 1: Create a program that ask 3 numbers (0-9) from the user.
#Step 2: Generate 3 random winning numbers (0-9)
#Step 3: Display “Winner” if all 3 input numbers matched the generated numbers
#Steo 4:  Display ”You loss” if not
#Step 5 Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit


import random


def trial ():
    user_Input = "yes"
    while user_Input [0] == "y":
        first = int (input ("Enter first number, from 0-9:  "))
        second = int (input ("Enter second number, 0-9:  "))
        third = int (input("Enter third number: "))

        gen1 = random.randint (0,9)
        gen2 = random.randint (0,9)
        gen3 = random.randint (0,9)

        score = 0

        if first == gen1 or gen2 or gen3:
            score += 1
        if second == gen1 or gen2 or gen3:
            score += 1
        if third == gen1 or gen2 or gen3:
            score += 1
        
        if score == 3:
            print ("Winner!")
        else:
            print ("You lose")
        
        user_Input = input ("Try again? y/n")
    else:
        exit ()


trial()


