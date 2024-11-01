# # SOAL 1
# import random

# def ambil_kartu():
#     """Menghasilkan kartu acak antara 1 dan 11 (nilai kartu Blackjack)"""
#     return random.randint(1, 11)

# def giliran_pemain():
#     total_kartu = ambil_kartu()
#     print(f"Kartu anda sekarang adalah: {total_kartu}")

#     while True:
#         pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
#         if pilihan == 'y':
#             kartu = ambil_kartu()
#             total_kartu += kartu
#             print(f"Kartu anda sekarang adalah: {total_kartu}")
#             if total_kartu > 21:
#                 print("Anda kalah, kartu anda melebihi 21.")
#                 return total_kartu, False
#         elif pilihan == 'n':
#             break
#         else:
#             print("Input tidak valid, masukkan 'y' atau 'n'.")

#     return total_kartu, True

# def giliran_dealer():
#     total_dealer = ambil_kartu()
#     print(f"Kartu dealer adalah: {total_dealer}")

#     while total_dealer < 17:
#         kartu = ambil_kartu()
#         total_dealer += kartu
#         print(f"Kartu dealer sekarang adalah: {total_dealer}")

#     if total_dealer > 21:
#         print("Dealer melebihi 21.")

#     return total_dealer

# def blackjack():
#     print("Selamat datang di Blackjack!")

#     total_pemain, pemain_aktif = giliran_pemain()
#     if not pemain_aktif:
#         return

#     total_dealer = giliran_dealer()

#     if total_dealer > 21 or total_pemain > total_dealer:
#         print("Anda menang!")
#     elif total_pemain == total_dealer:
#         print("Seri!")
#     else:
#         print("Dealer menang!")

# blackjack()

# ________________________________________________________________

# SOAL 2
import random
persent_jebakan = random.randint(1,20)
print(f"Persentase Jebakan: {persent_jebakan}")

def game():
    total_jarak = 0
    deteksi_bahaya = False
    while True:
        try:
            langkah = int(input("Masukkan angka (meter) atau tekan 0 untuk selesai: "))
            if  langkah == 0:
                print("Perjalanan dihentikan")
                break
            if langkah < 0:
                print("Masukkan bilangan BULAT POSITIF")
                break
            if langkah == persent_jebakan:
                deteksi_bahaya = True
            else:
                if langkah > 20:
                    deteksi_bahaya = True
            total_jarak += langkah
            print(f"Total jarak: {total_jarak}")
        except ValueError:
            print("Input tidak valid")

    if total_jarak > 0:
        print(f"Total jarak: {total_jarak}")
        if deteksi_bahaya == True:
            print(f"Bahaya: Ada")
        else:
            print("Bahaya: Tidak ada")
        if total_jarak == 50 and deteksi_bahaya == False:
            print("Aman. Kamu tepat menemukan harta karun dan menang!")
        elif deteksi_bahaya == True:
            print("Tidak aman untuk menggali harta karun. Coba lagi!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")
    # elif total_jarak == 0 and not ValueError:
        # print("Perjalanan dihentikan")

game()

# _________________________________________________________________

# SOAL 3
# def jikaGenap(n):
#     return n // 2
# def jikaGanjil(n):
#     return (n * 3) + 1
# def mathPuzzle():
#     try:
#         n = int(input("Masukkan bilangan bulat positif: "))
#         proses = 0
#         if n <= 0:
#             print("HANYA BILANGAN POSITIF YANG BOLEH DIINPUT!")
#         else:
#             while n > 1:
#                 if n % 2 == 0:
#                     n = jikaGenap(n)
#                 else:
#                     n = jikaGanjil(n)
#                 print(n)
#                 proses += 1
#             print(f"Jumlah langkah: {proses}")
#     except ValueError:
#         print("Input tidak valid")

# mathPuzzle()

# _________________________________________________________________

# SOAL 4
# def tambah(a, b):
#     return a + b
# def kurang(a, b):
#     return a - b
# def kali(a, b):
#     return a * b
# def bagi(a, b):
#     if b == 0:
#         return "Pembagian dengan 0 tidak diperbolehkan"
#     else:
#         return a / b
# def kalkulator():
#     print("Selamat datang di kalkulator sederhana!")
#     try:
#         a = float(input("Angka pertama: "))
#         b = float(input("Angka kedua: "))
#         operasi = input("Pilih operasi (+, -, *, /): ")
#         if operasi == "+":
#             print(f"{a} + {b} = {tambah(a,b)}")
#         elif operasi == "-":
#             print(f"{a} - {b} = {kurang(a,b)}")
#         elif operasi == "*":
#             print(f"{a} * {b} = {kali(a,b)}")
#         elif operasi == "/":
#                 print(f"{a} / {b} = {bagi(a,b)}")
#         else:
#             print("Operasi tidak valid. Gunakan +, -, *, atau /")
#     except ValueError:
#         print("Input tidak valid")

# kalkulator()