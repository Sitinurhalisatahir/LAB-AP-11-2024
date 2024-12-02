import random

angka_rahasia = random.randint(1, 100)
percobaan = 0
max_percobaan = 5 

print("Selamat datang di permainan tebak angka!")
print("ketik 0 jika ingin mengakhiri permainan.")

while percobaan < max_percobaan:
    try:
        tebakan = int(input(f"Percobaan ke-{percobaan + 1}: Masukkan tebakan Anda: "))
    except ValueError:
        print("Silakan masukkan angka yang valid.")
        continue
    
    if tebakan == 0:
        print("Anda telah menghentikan permainan. Terima kasih!")
        break
    
    percobaan += 1
    
    if tebakan > angka_rahasia:
        print("Angka terlalu besar. ")
    elif tebakan < angka_rahasia:
        print("Angka terlalu kecil. ")
    else:
        print(f"Selamat! Anda telah menebak angka {angka_rahasia} dengan benar!")
        break
else:
    print(f"Maaf, Anda telah kehabisan percobaan. Angka yang benar adalah {angka_rahasia}.")
