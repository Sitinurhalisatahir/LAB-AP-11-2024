daftar_barang = {}

def tambah_daftar(kode, nama, jumlah, harga):
    daftar_barang[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    print("Barang berhasil ditambahkan\n")

def hapus_barang(kode):
    if kode in daftar_barang:
        daftar_barang.pop(kode)
        print("Barang berhasil dihapus\n")
    else:
        print(f"Barang dengan kode {kode} tidak ditemukan\n")

def tampilkan_daftar():
    if daftar_barang:
        for key, value in daftar_barang.items():
            print(f"Kode: {key}, Nama: {value['nama']}, Jumlah: {value['jumlah']}, Harga: {value['harga']}")
    else:
        print("Daftar barang masih kosong\n")

def cari_barang(kode):
    if kode in daftar_barang:
        data = daftar_barang[kode]
        print(f"Kode: {kode}")
        print(f"Nama: {data['nama']}")
        print(f"Jumlah: {data['jumlah']}")
        print(f"Harga: {data['harga']}")
    else:
        print(f"Data dengan kode {kode} tidak ditemukan\n")

def update_barang(kode, nama, jumlah, harga):
    if kode in daftar_barang:
        daftar_barang[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print("Data barang berhasil diupdate\n")
    else:
        print(f"Barang dengan kode {kode} tidak ditemukan\n")

while True:
    try:
        print("\n===== DAFTAR INVENTORY BARANG =====")
        print("1. Tambah Daftar Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar Dari Menu")
        inputan = int(input(f"-->Pilih opsi (1-6): "))

        if inputan == 1:
            kode = int(input("\nMasukkan kode: "))
            if kode in daftar_barang:
                print(f"Barang dengan kode {kode} sudah ada. Gunakan kode lain\n")
            else:
                nama = input("Masukkan nama: ")
                jumlah = int(input("Masukkan jumlah: "))
                harga = int(input("Masukkan harga: "))
                tambah_daftar(kode, nama, jumlah, harga)

        elif inputan == 2:
            kode_clear = int(input("\nMasukkan kode barang yang ingin dihapus: "))
            hapus_barang(kode_clear)

        elif inputan == 3:
            tampilkan_daftar()

        elif inputan == 4:
            kode = int(input("\nMasukkan kode barang yang ingin dicari: "))
            cari_barang(kode)

        elif inputan == 5:
            kode = int(input("\nMasukkan kode barang yang ingin diupdate: "))
            if kode in daftar_barang:
                nama = input("Masukkan nama baru (klik ENTER untuk tetap): ") or daftar_barang[kode]['nama']
                jumlah = input("Masukkan jumlah baru (klik ENTER untuk tetap): ") or daftar_barang[kode]['jumlah']
                harga = input("Masukkan harga baru (klik ENTER untuk tetap): ") or daftar_barang[kode]['harga']
                update_barang(kode, nama, jumlah, harga)
            else:
                print(f"Barang dengan kode {kode} tidak ditemukan\n")

        elif inputan == 6:
            print("\n==== KELUAR DARI MENU ====\n")
            break
        else:
            print("Menu tidak tersedia. Pilih menu 1-6!\n")
    except ValueError as zee:
        print("Input tidak valid!")
        print(f"Error : {zee}\n")
        
