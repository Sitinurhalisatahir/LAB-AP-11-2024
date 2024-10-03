def konverter_kecepatan():
    # Daftar satuan kecepatan yang didukung
    satuan_list = ['m/s', 'km/h', 'mph', 'knot', 'mach']
    # Faktor konversi dari setiap satuan ke m/s
    konversi_ke_ms = [1, 1/3.6, 0.44704, 0.514444, 343]

    # Tampilkan judul program
    print("=" * 40)
    print("  Konverter Satuan Kecepatan")
    print("=" * 40)

    # Tampilkan pilihan satuan yang tersedia
    print("Pilihan satuan:")
    for i, satuan in enumerate(satuan_list, 1):
        print(f"{i}. {satuan}")
    print("=" * 40)

    try:
        # Minta input nilai kecepatan dari pengguna
        nilai = float(input("Masukkan nilai kecepatan: "))

        # Tampilkan pilihan satuan asal
        print("\nPilih satuan asal:")
        for i, satuan in enumerate(satuan_list, 1):
            print(f"{i}. {satuan}")
        pilihan_asal = int(input("Masukkan nomor pilihan asal: "))

        # Tampilkan pilihan satuan tujuan
        print("\nPilih satuan tujuan:")
        for i, satuan in enumerate(satuan_list, 1):
            print(f"{i}. {satuan}")
        pilihan_tujuan = int(input("Masukkan nomor pilihan tujuan: "))

        # Validasi pilihan satuan
        if pilihan_asal < 1 or pilihan_asal > len(satuan_list) or \
           pilihan_tujuan < 1 or pilihan_tujuan > len(satuan_list):
            raise ValueError("Pilihan tidak valid")

        # Ambil satuan dan faktor konversi berdasarkan pilihan
        satuan_asal = satuan_list[pilihan_asal - 1]
        satuan_tujuan = satuan_list[pilihan_tujuan - 1]
        faktor_konversi_asal = konversi_ke_ms[pilihan_asal - 1]
        faktor_konversi_tujuan = konversi_ke_ms[pilihan_tujuan - 1]

        # Konversi ke m/s sebagai satuan dasar
        base = nilai * faktor_konversi_asal

        # Hitung konversi ke semua satuan
        hasil = {}
        for i, satuan in enumerate(satuan_list):
            hasil[satuan] = base / konversi_ke_ms[i]

        # Hitung konversi spesifik ke satuan tujuan
        hasil_spesifik = base / faktor_konversi_tujuan

        # Tampilkan hasil konversi spesifik
        print("\nHasil Konversi Spesifik:")
        print(f"{nilai} {satuan_asal} = {hasil_spesifik:.4f} {satuan_tujuan}")

        # Tampilkan hasil konversi ke semua satuan
        print("\nHasil Konversi ke Semua Satuan:")
        print("-" * 40)
        print(f"{'Satuan':<10} {'Nilai':>15}")
        print("-" * 40)
        for satuan, nilai in hasil.items():
            print(f"{satuan:<10} {nilai:>15.4f}")
        print("-" * 40)

    except ValueError as e:
        # Tangani kesalahan input nilai atau pilihan tidak valid
        print(f"Error: {e}")
    except Exception as e:
        # Tangani kesalahan umum lainnya
        print(f"Terjadi kesalahan: {e}")

# Jalankan fungsi
konverter_kecepatan()

