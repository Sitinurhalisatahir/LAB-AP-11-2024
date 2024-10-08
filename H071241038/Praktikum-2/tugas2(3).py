nilai_akhir = int(input("masukkan nilai akhir:"))
persentase_kehadiran = int(input("masukkan persentase kehadiran: "))

if nilai_akhir >= 85 and nilai_akhir <= 100 and persentase_kehadiran >= 75:
  print("lulus dengan predikat A")
elif nilai_akhir >= 70 and nilai_akhir <= 84 and persentase_kehadiran >= 75:
  print("lulus dengan predikat B")
elif nilai_akhir >= 60 and nilai_akhir <= 69 and persentase_kehadiran >= 75:
  print("lulus dengan predikat C")
else:  
  nilai_tugas_tambahan = int(input("masukkan nilai tambahan"))
  if nilai_akhir <= 60 and nilai_tugas_tambahan >= 70 and persentase_kehadiran >= 75:
    print("lulus dengan predikat C")
  else:
    print("tidak lulus")
