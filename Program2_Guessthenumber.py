#Steps:
#Step 1: Generate 1 random number (0-100)
#Step 2: Ask the user to guess the number
#Step 3: Display “Greater than” if the inputed number is greater than the random number
#Step 4: Display “Less than” if the inputed number is less than the random number
#Step 5: Repeat asking the user until the random number has been guessed correctly.

import random

random_Number = random.randint (0, 100)
print (f"{random_Number}")

def check_Number (random_Number):
    user_Input = int (input (f"What is the number?  "))
    while user_Input != random_Number:
        if user_Input < random_Number:
            print ("Less than")
            user_Input = int (input(f"What is the number?  "))
        if user_Input > random_Number:
            print ("Greater than")
            user_Input = int (input(f"What is the number?  "))
    else:
        print (f"Correct! Random number is {random_Number}")


check_Number (random_Number)


