karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

hasil = f"Karakter {karakter} merupakan bagian dari kalimat {kalimat}" * (karakter in kalimat) or f"{karakter} tidak ditemukan dalam '{kalimat}'" * (karakter not in kalimat)

print(hasil)