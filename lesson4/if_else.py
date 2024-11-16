"""
IF Else

If else adalah  pernyataan dengan 2 kondisi misal untuk benar dan salah
"""
import random

first_number = random.randrange(1,100)
second_number = random.randrange(1,100)
third_number = random.randrange(1,100)
fourth_number = random.randrange(1,100)

addition = first_number + second_number
subtraction = third_number - fourth_number
print("Check your math skill!")

print(f" Addition : {first_number} + {second_number}")
addition_answer = input("Your answer : ") # Parse dulu ke integer karena ketika input dia default tipe datanya string

print(f" Subtraction : {third_number} - {fourth_number}")
subtraction_answer = input("Your answer : ")

if int(addition_answer) == addition and int(subtraction_answer) == subtraction:
    print(f"Correct! the answer is {addition_answer},{subtraction_answer}")
else:
    print(f"wrong answer!, double check your answer")

