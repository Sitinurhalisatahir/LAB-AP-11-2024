
nilai_akhir = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))


if kehadiran < 75:
    print("Tidak Lulus karena kehadiran tidak mencukupi")
else:
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A")
    elif 70 <= nilai_akhir <= 84:
        print("Lulus dengan Predikat B")
    elif 60 <= nilai_akhir <= 69:
        print("Lulus dengan Predikat C")
    else:
        tugas_tambahan = input("Apakah semua tugas tambahan dinilai di atas 70? (ya/tidak): ").lower()
        if tugas_tambahan == "ya" and kehadiran >= 75:
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")