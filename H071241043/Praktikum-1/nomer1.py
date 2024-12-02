# Input harga saham kemarin
harga_kemarin           = float(input("Masukkan harga saham kemarin: "))

harga_hari_ini          = 105.0
rekomendasi_list        = ["Jual", "Tahan", "Beli"]

perubahan_persentase    = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

result                  = rekomendasi_list[(perubahan_persentase > -3) + (perubahan_persentase > 5)]

# Menampilkan hasil
print(f"Perubahan persentase harga saham: {perubahan_persentase:.2f}%")
print(f"Rekomendasi: {result}")
 
 


