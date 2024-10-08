harga_kemarin = int(input("Masukkan harga kemarin : "))
harga_hari_ini = 105.0

persentase_perubahan = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

hasil = "Beli" * (persentase_perubahan > 5) + \
        "Tahan" * (persentase_perubahan < 5) * (persentase_perubahan > -3)+ \
        "Jual" * (persentase_perubahan < -3)

print (hasil)
print (f"{persentase_perubahan:.2f}")

