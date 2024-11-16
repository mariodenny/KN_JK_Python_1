"""
Assignment operator adalah function dan tidak bisa langsung di print
jadi harus di inisialisasi. Nilai yang diinisialisasi akan dirubah sesuai dengan yang di assign
misal dibawah ini number1 nilainya 2 number2 nilainya 3
saat di assign my_number1 maka nilai nya akan berubah

"""

my_number1 = 2
my_number2 = 3

print(f"my first number is: {my_number1}")
print(f"my second number is: {my_number2}")
print(my_number1)  # 2
my_number1+=my_number2 # 5

print(my_number1)

