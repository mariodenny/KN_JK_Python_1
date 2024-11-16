"""
                NAME : KODINGNEXT
                DATE : 2024-11-16
                PROJECT : GUESS MY NUMBER
"""

import  random

# Range of number will be guessed
guess_number = random.randrange(1,3)

#statement
print("guess my number from 1 to 3")
your_guess = input("can you guess what my number is ? : ")

print("The number is...")
print(guess_number == int(your_guess))
print(f"The number is {str(guess_number)}")

