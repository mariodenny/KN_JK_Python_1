"""
IF ELIF ELSE

adalah flow control atau conditional statement yang memiliki lebih dari 2 kondisi. Yang paling umum ditemui adalah
lampu lalu lintas

JIKA
    lampu_hijau = jalan
JIKA
    lampu_kuning = bersiap
JIKA
    lampu_merah = berhenti
ELSE
    lampu tidak ada!

Kita terapkan ke dalam python jadi seperti berikut


                            NAME : KODINGNEXT
                            DATE : 2024-11-16
                            PROJECT : TRAFFIC LIGHT
"""
light_color = input("Input color : ")

if light_color == "red" :
    print(f"traffic lamp color is {light_color}, which mean stop!")
elif light_color == "green":
    print(f"traffic lamp color is {light_color}, which mean go!")
elif light_color == "yellow":
    print(f"traffic lamp color is {light_color}, which mean be ready!")
else:
    print(f"your {light_color}  color, doesnt exists!")
