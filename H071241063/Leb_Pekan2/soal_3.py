#INPUT DARI PENGGUNA
nilai_akhir = int(input("Masukkan nilai akhir : "))
kehadiran = int(input("Masukkan persentase kehadiran : "))

# KONDISI KEHADIRAN BATAS 75%
if kehadiran < 75:
    print("Tidak Lulus karena kehadiran kurang dari 75%")
else:

    # MENETUKAN A,B,C DAN TIDAK LULUS BERDASARKAN NILAI
    if nilai_akhir >= 85:
        print("Lulus dengan Predikat A")
    elif nilai_akhir >= 70:
        print("Lulus dengan Predikat B")
    elif nilai_akhir >= 60:
        print("Lulus dengan Predikat C")
    else:
        # KONFIRMASI TUGAS TAMBAHAN
        tugas_tambahan = input("Apakah tugas tambahan selesai dengan nilai di atas 70? (y/n): ")
        if tugas_tambahan == "y":
            print("Lulus dengan Predikat C")
        else:
            print("Tidak Lulus")
