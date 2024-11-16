"""
    Conditional Statement

    Conditional statement adalah suatu pernyataan yang akan dijalankan memenuhi syarat. Contohnya IF(jika)

"""
import random

my_random_number = random.randrange(1,100)

print("This is random number generator. We have a variable with a random value from 1 to 100 inside of it")
print("If the number is less than 50 , we'll let you know")

print(f"The random number is {my_random_number}")
# Conditional statement
if my_random_number < 50:
    print(f"Yes! the random number is less than 50!")