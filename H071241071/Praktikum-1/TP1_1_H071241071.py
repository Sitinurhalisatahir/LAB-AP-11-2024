harga_kemarin = float(input("Masukkan harga saham kemarin : "))
harga_hari_ini = (105)
perubahan_persentase = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
print(f"Perubahan persentase harga saham: {perubahan_persentase:.2f}%")
rekomendasi = ("Jual", "Tahan", "Beli")[(perubahan_persentase > 5) - (perubahan_persentase < -3) + 1]
print(f"Rekomendasi investasi: {rekomendasi}")
