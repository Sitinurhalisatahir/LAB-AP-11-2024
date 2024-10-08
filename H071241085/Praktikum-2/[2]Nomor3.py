
nilai_akhir = int(input('Masukkan nilai akhir : '))
kehadiran = int(input('Masukkan presentase kehadiran : '))
# tugas_tambahan = input('Kerja tugas tambahan? : ')

'''menentukan predikat kelulusan dengan
kondisi nilai dan kehadiran siswa  tersebut'''
if kehadiran < 75:
    print('Tidak lulus (kehadiran kurang)')
elif nilai_akhir >= 85:
    print('lulus dengan predikat A')
elif nilai_akhir >= 70:
    print('Lulus dengan predikat B')
elif nilai_akhir >= 60:
    print('Lulus dengan predikat C')
else:
    tugas_tambahan = input('Kerja tugas tambahan? : ')
    if tugas_tambahan == 'ya':
        print('Lulus dengan predikat c')
    else:
        print('Tidak lulus')

    # if tugas_tambahan == 'ya':
    #     print('Lulus dengan predikat C')