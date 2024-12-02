usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota (ya/tidak): ")

if usia < 5:
  harga_dasar = 0
elif 5 <= usia <= 12:
  harga_dasar = 50000
elif 13 <= usia <= 59:
  harga_dasar = 100000
else:
  harga_dasar = 70000

harga_akhir = int(harga_dasar * 0.8) if anggota == "ya" else harga_dasar

if harga_akhir == 0 :
  print("Harga tiket : Gratis ")
else : 
  print("Harga tiket: Rp.", harga_akhir)