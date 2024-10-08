import random

Jawaban = random.randint(1, 100)
percobaan = 5

for i in range(percobaan):
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
    
    if i == percobaan - 1:
        print(f"Anda kehabisan percobaan. Jawabannya adalah {Jawaban}.")