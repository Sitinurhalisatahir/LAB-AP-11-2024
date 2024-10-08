# SOAL 1 <MENGIDENTIFIKASI JENIS SEGITIGA>
a = float(input("Panjang sisi pertama: "))
b = float(input("Panjang sisi kedua: "))
c = float(input("Panjang sisi ketiga: "))

segitiga_samasisi = a == b == c
segitiga_samakaki = a == b or b == c or c == a
segitiga_sembarang = a+b>c and a+c>b and b+c>a

if a<=0 or b<=0 or c<=0:
    hasil = "Tidak dapat membentuk segitiga yang valid"
elif not segitiga_sembarang:
    hasil = "Tidak dapat membentuk segitiga yang valid"
else:
    if segitiga_samasisi:
        hasil = "Segitiga sama sisi"
    elif segitiga_samakaki:
        hasil = "Segitiga sama kaki"
    elif segitiga_sembarang:
        if a != b != c:
            hasil = "Segitiga Sembarang"
print(f"Hasil: {hasil}")

# _________________________________________________________

# # SOAL 2 <HARGA TIKET MASUK WAHANA BERMAIN>
# usia = int(input("Masukkan usia: "))

# if usia < 5:
#     print("Gratis tiket masuk.")
# else:   
#     keanggotaan = input("Apakah anda anggota (ya/tidak)?: ")
#     if usia >= 5 and usia <= 12:
#         harga = 50000
#     elif 13 <= usia <= 59:
#         harga = 100000
#     else:
#         harga = 70000

#     harga_diskon = harga * 20//100
#     total = harga - harga_diskon if keanggotaan == "ya" else harga
#     print(f"Harga tiket anda: Rp. {total}")

# _________________________________________________________

# # SOAL 3 <SISTEM PENENTUAN KELULUSAN>
# nilai = int(input("Masukkan nilai akhir: "))
# kehadiran = int(input("Masukkan persentase kehadiran: "))
# a = range(85,101)
# b = range(70,85)
# c = range(60,70)

# if kehadiran >= 75:
#     if nilai in a:
#         print("Anda lulus dengan predikat A")
#     elif nilai in b:
#         print("Anda lulus dengan predikat B")
#     elif nilai in c:
#         print("Anda lulus dengan predikat C")
#     #Jika nilai kurang dari 60
#     elif nilai < 60:
#         chance = input("Nilai anda kurang, Apakah anda telah menyelesaikan semua tugas tambahan dengan baik (ya/tidak)? ")
#         if chance == "ya":
#             nilaiTambahan = int(input("Berapa nilai tugas tambahan anda: "))
#             if nilaiTambahan > 70:
#                 print("Anda lulus dengan predikat C-")
#             else:
#                 print("MAAF, ANDA MUSTAHIL LULUS.")
#         else:
#             print("MAAF, ANDA MUSTAHIL LULUS.")
# else:
#     print("Maaf, anda tidak lulus karena persentase kehadiran kurang dari 70%.")
    
# _________________________________________________________

# # SOAL 4 <MENENTUKAN PAKET LAYANAN INTERNET>
# data = int(input("Masukkan jumlah data yang digunakan: "))
# waktuPenggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
# jenisPengguna = input("Apakah anda pengguna Personal atau Bisnis? ")

# # penggunaan data
# ringan = data < 10
# sedang = 10 <= data <= 50
# berat = data > 50

# rekomend = None

# if jenisPengguna == "personal":
#     if waktuPenggunaan == "peak":
#         if sedang:
#             rekomend = "Paket B"
#         elif berat:
#             rekomend = "Paket C"
#     else: #off peak
#         if ringan:
#             rekomend = "Paket A"
# else: #bisnis
#     if waktuPenggunaan == "peak":
#         if berat:
#             rekomend = "Paket C"
#     else: #off peak
#         if berat:
#             rekomend = "Paket D"

# if rekomend:
#     print(f"Paket yang direkomendasikan adalah {rekomend}")
# else: #rekomend masih tidak bernilai
#     print("Tidak ada paket yang cocok")