usia = int(input("Masukkan usia anda: "))
anggota = input("Apakah anda anggota? (ya/tidak): ")

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

harga = harga * 0.8 if anggota.lower() == "ya" else harga

print("harga tiket: Rp", int(harga))