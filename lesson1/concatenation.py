"""
String concatenation
"""
my_name = "Denny Mario"
my_age = 24
is_married = False

# Old way python using + to concat

print("My name is " + my_name + " and i am : " + str(my_age)+ " years old")

# New way to concat from python 3.6 and latest
# Gunakan f string formatting untuk versi python terbaru karena lebih cepat,lebih mudah dibaca
intro = f"Hello my name is {my_name}, my age: {my_age}, i am {'Married' if is_married else 'Not Married' }"

print(intro)

# test shorthand

my_intro = "My name is "+ my_name + ", i am " + str(my_age) + " old, i am " + ("Married" if is_married else "Not Married")

print(my_intro)