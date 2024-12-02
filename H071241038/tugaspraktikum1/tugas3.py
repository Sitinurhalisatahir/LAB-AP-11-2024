# Input jumlah detik dari pengguna
total_detik = int(input("Masukkan jumlah detik: "))

# Hitung jam, menit, dan detik
jam = total_detik // 3600
menit = (total_detik % 3600) // 60
detik = total_detik % 60

# Format hasil sebagai jam:menit:detik dengan format 2 digit
waktu_format = f"{jam:2}:{menit:2}:{detik:2}"

# Tampilkan hasil
print("Waktu:", waktu_format)
