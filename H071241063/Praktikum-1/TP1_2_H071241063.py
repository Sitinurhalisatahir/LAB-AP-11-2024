karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

hasil = f'arakter merupakan bagian dari Kalimat' * (karakter in kalimat) + \
        f'{karakter} tidak ditemukan dalam "{kalimat}"' * (karakter not in kalimat)

print(hasil)
