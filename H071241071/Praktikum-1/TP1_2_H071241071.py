karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")
print(f'{karakter} merupakan bagian dari "{kalimat}"' * (karakter in kalimat) + f'{karakter} tidak ditemukan dalam "{kalimat}"' * (karakter not in kalimat))