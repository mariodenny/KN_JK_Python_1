"""
use all previous lesson to this project
"""

myFirstNumber = "30"
mySecondNumber = "6"
dividedNumber = int(myFirstNumber) / int(mySecondNumber)
multiplyNumber = int(myFirstNumber) * int(mySecondNumber)
addNumber = int(myFirstNumber) + int(mySecondNumber)
deductNumber = int(myFirstNumber) - int(mySecondNumber)

print("My first number is : " + myFirstNumber)
print("My second number is : " + mySecondNumber + "\n")

print(f"The result of dividing first number and second number is {dividedNumber}")
print(f"The result of multiplying first number and second number is {multiplyNumber}")
print(f"The result of adding first number and second number is {addNumber}")
print(f"The result of deducting first number and second number is {deductNumber}")

def my_word(number):
    print(f"Your number is {int(number)}")


my_word(2.5)