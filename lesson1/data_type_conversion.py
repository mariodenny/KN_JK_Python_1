"""
Data type conversion / type casting

sebuah tipe data dapat diubah (casting) ke tipe data lain nya dengan syarat tipe data yang
akan diubah itu memenuhi syarat tipe data yang akan diubah.
misal tipe data string 1 bisa diubah ke integer 1. karena 1 adalah angka
tapi jika ada string a tidak bisa diubah jadi integer a karena pada dasarnya a bukanlah angka
"""
number1 = "1"
number2 = 2
number3 = "a"

print(int(number1) + number2)
print(number3)
print(number1+number3)
