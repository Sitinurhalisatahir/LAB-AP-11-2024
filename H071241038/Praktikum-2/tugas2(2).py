usia = int(input("masukkan usia: "))
keanggotaan = input("apakah anda anggota? (ya/tidak): ")

if usia <= 5:
  harga = 0
elif usia >= 5 and usia <= 12:
  harga = 50000
elif usia >= 13 and usia <= 59:
  harga = 100000
elif usia >= 60:
  harga = 70000

diskon = harga - (harga *20/100)
harga_tiket = diskon if keanggotaan == "ya" else harga
print(f"harga tiket: {harga_tiket}")

