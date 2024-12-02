nilai_akhir = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))

if kehadiran < 75:
  print("Tidak Lulus (Kehadiran kurang)")
elif nilai_akhir >= 85:
  print("Lulus dengan Predikat A")
elif nilai_akhir >= 70:
  print("Lulus dengan Predikat B")
elif nilai_akhir >= 60:
  print("Lulus dengan Predikat C")
else:
  tugas_tambahan = int(input("Masukkan seluruh nilai rata-rata tugas tambahan: "))

  if tugas_tambahan > 70:
    print("Lulus dengan Predikat C")
  else:
    print("Tidak Lulus")