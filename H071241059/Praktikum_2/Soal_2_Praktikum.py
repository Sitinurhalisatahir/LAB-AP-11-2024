usia = int(input('Masukkan usia: '))

if usia < 5:
    print("Harga Tiket : Gratis")
else :
    anggota = input('Apakah Anda anggota (ya/tidak): ')
    diskon = 0.20
    if 5 <= usia <= 12:
        hargaawal = 50000
    elif 12 < usia < 60 :
        hargaawal = 100000
    else:
        hargaawal = 70000
    hargaakhir = hargaawal - (hargaawal*diskon)
    print(f'Harga Tiket: Rp. {hargaakhir:.0f}')