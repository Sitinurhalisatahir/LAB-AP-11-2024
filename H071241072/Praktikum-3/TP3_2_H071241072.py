import random

angka_rahasia = random.randint(1, 100)

print("Tebak angka antara 1 sampai 100.")

for i in range(5):
    tebak = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebak == 0:
        break
    elif tebak < angka_rahasia:
        print("Angka terlalu kecil.")
    elif tebak > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break
if tebak == 0:
    print(f"Anda memilih untuk berhenti. Angka rahasianya adalah {angka_rahasia}")
elif tebak != angka_rahasia:
    print(f"Anda kehabisan percobaan. Angka rahasianya adalah {angka_rahasia}")