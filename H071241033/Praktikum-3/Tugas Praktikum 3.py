# SOAL 1
# n = int(input("Masukkan nilai n: "))
# if n <= 2:
#     print("Bilangan yang anda input tidak dapat dijalankan.")
# else:
#     tengah = n//2
#     for i in range(1,tengah+1+(n%2)):
#         print("  "*(tengah-i+1) + "* "*(2*i-1))
#     for i in range(tengah,0,-1):
#         print("  "*(tengah-i+1) + "* "*(2*i-1))

# ____________________________________________________________________________

# # SOAL 2
import random
jawaban = random.randint(1,100)
max_try = 1

print("Tebak satu angka di antara 1 sampai 100")
print("Maksimal lima kali percobaan")
print(jawaban)

while max_try <= 5:
    try:
        input_user = int(input(f"Masukkan tebakan anda (input 0 untuk berhenti): "))
        if input_user == 0:
            print("Program dihentikan")
            break
        if input_user not in range(1,101):
            print("Angka di luar 1-100")
        else:
            if input_user == jawaban:
                print(f"Selamat, anda menebak angka yang benar")
                print(f"{input_user} adalah jawabannya")
                break
            elif input_user < jawaban:
                print("Angka terlalu kecil")
            else: #input_user > jawaban
                print("Angka terlalu besar")
    except ValueError:
        print("Angka yang anda input tidak valid")
    max_try += 1
else:
    print("Kesempatan anda untuk menebak telah habis")
    print(f"Jawabannya adalah {jawaban}")

# __________________________________________________________________________________

# SOAL 3
# n = int(input("Masukkan jumlah N: "))
# m = int(input("Masukkan jumlah M: "))

# for x in range(n):
#     if x % 2 == 0:
#         for y in range(m):
#             print(f"MOVE to ({x},{y})")
#     else:
#         for y in range(m-1,-1,-1):
#             print(f"MOVE to ({x},{y})")

# __________________________________________________________________________________

# SOAL 4
# list_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
# harga = int(input("Masukkan total harga: "))
# jumlah_uang = int(input("Masukkan uang yang diberikan: "))

# kembalian = jumlah_uang - harga
# if jumlah_uang < harga:
#     print("Uang tidak cukup")
# else:
#     for pecahan in list_pecahan:
#         lembar_pecahan = kembalian//pecahan
#         if lembar_pecahan>0:
#             print(f"{lembar_pecahan} lembar uang {pecahan}")
#             kembalian %= pecahan


# __________________________________________________________________________________

# SOAL 5
# a = int(input("Masukkan populasi awal hewan A: "))
# b = int(input("Masukkan populasi awal hewan B: "))
# hari = int(input("Masukkan jumlah hari: "))
# for h in range(1,hari+1):
#     if h % 2 == 0:
#         a -= int(20/100*a)
#         b -= int(40/100*b)
#     else: #hari % 2 == 1
#         a += int(30/100*a)
#         b += int(50/100*b)
#     if h % 5 == 0:
#         a -= int(10/100*a)
#         b -= int(10/100*b)
#         print(f"Hari {h}. Predator memakan 10% populasi")
#     print(f"Hari {h}. Serangga A: {a}, Serangga B: {b}")

# _________________________________________________________________________________