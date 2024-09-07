harga_hari_ini = 105.0
harga_kemarin = float(input("Masukkan harga saham kemarin: "))
persentase_perubahan = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi = {
    1: "Beli",
    2: "Tahan",
    3: "Jual"
}

rekomendasi = rekomendasi[
    (persentase_perubahan > 5) * 1 + (persentase_perubahan >= -3 and persentase_perubahan <=5) * 2 + (persentase_perubahan < -3) * 3
]

print("Perubahan Persentase Harga Saham: {persentase_perubahan:.2f}%")
print(f"Rekomendasi Investasi: {rekomendasi}")