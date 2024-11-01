harga_saham_kemarin = float(input("Masukkan harga saham kemarin: "))
harga_saham_hari_ini = 105.0

perubahan_persentase = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100

beli = (perubahan_persentase > 5) * 1
tahan = (-3 <= perubahan_persentase <= 5 ) * 1
jual = (perubahan_persentase < -3 ) * 1

rekemondasi = beli * "beli" + tahan * "tahan" + jual * "jual"


print(f"perubahan persentase: {perubahan_persentase: .2f}%")
print(f"rekomendasi investasi: {rekemondasi}")