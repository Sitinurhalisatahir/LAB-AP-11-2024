import random
angka_random = random.randint(1, 100)
percobaan = 0
max_percobaan = 5

while percobaan < max_percobaan:
    try:
        tebakan = int(input("masukkan tebakan anda (0 untuk berhenti): "))
        if tebakan == 0:
            break
        percobaan += 1
        if tebakan > angka_random:
            print("Angka terlalu besar!")
        elif tebakan < angka_random:
            print("Angka terlalu kecil!")
        else:
            print(f"Selamat! Anda berhasil menebak angka rahasia {angka_random} dalam {percobaan} kali percobaan.")
            break
    except ValueError:
        print("Masukkan angka yang valid.")
    
if percobaan == max_percobaan and tebakan != angka_random:
    print(f"Maaf, Anda telah kehabisan percobaan. Angka rahasia adalah {angka_random}. Terima kasih telah bermain!")