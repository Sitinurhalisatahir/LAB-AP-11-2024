# # SOAL 1
# saham_kemarin = float(input("Masukkan harga saham kemarin: "))
# saham_hariIni = 105.0 

# perubahan = (saham_hariIni - saham_kemarin) / saham_kemarin * 100
# print(f"Perubahan persentase harga saham: {perubahan:.2f}%")

# beli = perubahan > 5
# tahan = -3 <= perubahan <= 5
# jual = perubahan < -3

# rekomendasi = beli * "Beli" + tahan * "Tahan" + jual * "Jual"
    
# print(f"Rekomendasi investasi: {rekomendasi}.")




# # # SOAL 2
# karakter = input("Masukkan karakter: ")
# kalimat = input("Masukkan kalimat: ")

# karakter_lower = karakter.lower()
# kalimat_lower = kalimat.lower()

# cari = karakter_lower in kalimat_lower
# output = (cari) and f"{karakter} merupakan bagian dari \"{kalimat}\"" or f"{karakter} bukan bagian dari \"{kalimat}\""
# print(output)
# if karakter_lower in kalimat_lower:
#     output = (f"'{karakter}' merupakan bagian dari '{kalimat}'.")
# else:
#     output = (f"'{karakter}' tidak ditemukan dalam '{kalimat}'.")





# SOAL 3
print("KONVERSI DETIK KE JAM")
input_detik = int(input("Masukkan jumlah detik: "))

jam = input_detik // 3600
sisa_detik = input_detik % 3600
menit = sisa_detik //60
detik = sisa_detik % 60

print(f"Waktu dalam format \"jam:menit:detik\" adalah:\n{jam:02d}:{menit:02d}:{detik:02d}")





# SOAL 4
print("Konversi suhu dari skala Celsius ke Kelvin, Reamur, dan Fahrenheit")
celsius = float(input("Masukkan suhu dalam celcius:"))

kelvin = celsius + 273
reamur = celsius * 4 / 5
fahrenheit = celsius * 9 / 5 + 32

print(f"Hasil konversi dari suhu {celsius} Celsius ke Kelvin adalah {kelvin} K.")
print(f"Hasil konversi dari suhu {celsius} Celsius ke Reamur adalah {reamur} R.")
print(f"Hasil konversi dari suhu {celsius} Celsius ke Fahrenheit adalah {fahrenheit} R.")
