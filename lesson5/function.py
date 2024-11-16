"""
Function adalah cara untuk menyederhanakan kode, misal kita mau cetak 5 nama orang,
Kalau menggunakan metode sebelumnya yang dipelajari
maka kita harus ketik
print() sebanyak 5 kali
dengan function bisa di sederhanakan. cukup panggil saja function nya tanpa harus ketik
print sebanyak banyaknya

return di function dipakai untuk mulangin hasil nya secara langsung , jadi function as value.
"""

# Basic function
def greetings():
    print("Hello,Mom!")

# Function with param
def add_numbers(num_a,num_b):
    result = num_a + num_b
    print(f"The result is {result}")

# Function using return
def subtract_numbers(num_a,num_b):
    return num_a - num_b

# Example soal latihan, mencari luas persegi panjang

"""
PSEUDOCODE

luas = panjang * lebar

def rectangle_area(length , width):
    result = length * width
    print(f"Rectangle area length {length} * width{width} = {result}")
"""
# Contoh soal
def rectangle_area(length , width):
    result = length * width
    print(f"Rectangle area length {length} * width {width} = {result}")

# Recursive function

"""
factorial : 5! = 5x4x3x2x1
PSEUDOCODE

fungsi factorial(n -> banyaknya nilai) :
        jika n == 1:
            return 1
        else 
            return n * factorial(n-1)
            misal n = 5
            maka yang terjadi
            5 * factorial(5-1)
            5 * factorial(4)
            kan dia return value , jadinya factorial pertama adalah 5-1 = 4
            5 * 4
            
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) # memanggil fungsi yang berupa dirinya sendiri


# Call function
add_numbers(10,2)
add_numbers(2,3)
add_numbers(6,8)
print(f"The return function result : {subtract_numbers(10, 1)}")
rectangle_area(10,8)
rectangle_area(2,1)
rectangle_area(6,4)

print(f" result of factorial {factorial(3)}")