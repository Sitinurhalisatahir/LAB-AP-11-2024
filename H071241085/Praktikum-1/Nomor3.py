import math

print("~~~Konversi detik ke jam~~~")
detikInput = int(input("Masukkan jumlah detik: "))

#jam = math.floor((detikInput - (detikInput % 3600)) / 3600)
#menit = math.floor(detikInput % 3600 / 60)
#detik = detikInput % 60

jam = detikInput // 3600
menit = ((detikInput % 3600)//60)
detik = detikInput % 60

print(f"{jam:02}:{menit:02}:{detik:02}")

