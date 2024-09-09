  # Input harga saham kemarin dan harga hari ini
harga_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105.0  # Harga hari ini sudah diketahui

# Menghitung perubahan persentase
perubahan_persentase = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

beli = perubahan_persentase > 5
tahan = perubahan_persentase > -3 and perubahan_persentase < 5
jual = perubahan_persentase < -3

print(f"Perubahan persentase: {perubahan_persentase:.2f}%")
print("Rekomendasi Invenstasi : ", {True: "Beli", False: ""}[beli], {True: "Tahan", False: ""}[tahan], {True: "Jual", False: ""}[jual])
