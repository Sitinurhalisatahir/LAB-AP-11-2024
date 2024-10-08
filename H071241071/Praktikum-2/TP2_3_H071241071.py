Nilai_Akhir = int(input("Masukkan nilai akhir : "))
RataRata_Nilai_Tugas_Tambahan = int(input("Masukkan rata-rata nilai tugas tambahan : "))
Kehadiran = int(input("Masukkan persentase kehadiran : "))

if 85 <= Nilai_Akhir <= 100 and 75 <= Kehadiran <= 100 :
    print("Lulus dengan predikat A")
elif 70 <= Nilai_Akhir <= 84 and 75 <= Kehadiran <= 100 :
    print("Lulus dengan predikat B")
elif 60 <= Nilai_Akhir <= 69 and 75 <= Kehadiran <= 100 :
    print("Lulus dengan predikat C")
elif Nilai_Akhir < 60 and 70 <= RataRata_Nilai_Tugas_Tambahan <= 100 and 75 <= Kehadiran <= 100 :
    print("Lulus dengan predikat C")
else :
    print("Tidak Lulus")
