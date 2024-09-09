karakter = input("Masukkan karakter: ")
Kalimat = input("Masukkan kalimat: ")

hasil_list = ["Karakter tidak ditemukan dalam Kalimat", "Karakter merupakan bagaian dari Kalimat"]
hasil_index = (karakter in Kalimat)
hasil = hasil_list[hasil_index] 

print(hasil)
