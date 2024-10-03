import random

Jawaban = random.randint(1, 100)

Try = 0
Maxtry = 5

while Maxtry != Try :
    tebakan = int(input("Masukkan tebakan Anda (ketik '0' untuk berhenti): "))
    if tebakan == 0:
        print("Anda menghentikan permainan.")
        break
    
    if tebakan == Jawaban:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > Jawaban:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    Try = Try+1
else :
    print("Kesempatan anda telah habis")
