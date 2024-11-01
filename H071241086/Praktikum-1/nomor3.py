detik = int(input ("Masukkan Jumlah detik: "))

jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60

print(f"{jam:02d}: {menit:02d}:{detik:02d}")    
