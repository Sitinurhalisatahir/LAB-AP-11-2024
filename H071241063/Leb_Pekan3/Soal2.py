import random

rahasia = random.randint(1, 100)
print(rahasia)
for i in range(5):
    tebak = input(f"Masukkan Tebakan Anda ke-{i+1} (0 untuk berhenti): ")
    if tebak == '0':
        print("Permainan dihentikan.")
        break
    tebak = int(tebak)
    if tebak == rahasia:
        print("Selamat! Anda menebak dengan benar.")
        break
    print("Angka terlalu", "besar." if tebak > rahasia else "kecil.")
else:
    print(f"Maaf, Anda kehabisan kesempatan. Angka yang benar adalah {rahasia}.")