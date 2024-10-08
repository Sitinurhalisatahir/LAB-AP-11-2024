Usia = int(input("Masukkan usia : "))
Anggota = input("Apakah Anda anggota ya/tidak : ")
if Usia < 5:
    Harga = 0
elif 5 <= Usia <= 12:
    Harga = 50000
elif 13 <= Usia <= 59:
    Harga = 100000
else:
    Harga = 70000

Harga_Akhir = Harga * 0.80 if Anggota == "ya" else Harga

if Harga_Akhir == 0 :
    print("Harga tiket : Gratis")
else : 
    print(f'Harga tiket : {Harga_Akhir}')