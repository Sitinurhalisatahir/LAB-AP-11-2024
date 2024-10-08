#INPUT DARI PENGGUNA
usia = int(input("Masukkan usia : "))
anggota = input("Apakah Anda anggota (ya/tidak): ")

#KONDISI HARGA BERDASARKAN USIA
if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

#BAGIAN DISKON
harga = harga * 0.8 if anggota == "ya" else harga

#TAMPILAN HASIL
print(f"Harga tiket: Rp {harga}")
