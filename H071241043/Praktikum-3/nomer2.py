import random

angka_rahasia = random.randint(1,100)

for i in range(5) :
    tebakan = int(input("Masukkan angka : "))
   
    if tebakan == angka_rahasia:
        print("SELAMAT, ANGKA BENAR!")
        break
    elif tebakan == 0:
        print()
        break
    elif tebakan > angka_rahasia :
        print("angka terlalu besar")
    elif tebakan < angka_rahasia :
        print("angka terlalu kecil")

    if i == 4:
        print(f"Kesempatan anda telah habis. Angka rahasia adalah {angka_rahasia}")

 

