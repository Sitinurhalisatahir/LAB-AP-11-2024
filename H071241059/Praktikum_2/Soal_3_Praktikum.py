nilaiakhir = int(input('Masukkan nilai akhir: '))
kehadiran = int(input('Masukkan persentase kehadiran: '))

if nilaiakhir >= 60 :
    if 85 <= nilaiakhir <= 100 and kehadiran >= 75 :
        print('Lulus dengan Predikat A')
    elif 70 <= nilaiakhir < 85 and kehadiran >= 75:
        print('Lulus dengan Predikat B')
    elif 60 <= nilaiakhir < 70 and kehadiran >= 75:
        print('Lulus dengan predikat C')
    elif nilaiakhir > 100:
        print('Tidak Valid')
elif nilaiakhir < 60 and kehadiran >= 75:
    tugas_tambahan = int(input('Masukkan Nilai Tambahan: '))
    lulusbersyarat = (nilaiakhir + tugas_tambahan)/2
    print('Lulus dengan predikat C')
else:
    print('Tidak Lulus')