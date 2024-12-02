barang = []

def menu():
    while True:
        print("=== Menu Inventory Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

def tambah_barang():
    kode = input("Masukkan kode barang: ")

    if  not kode:
        print("Kode barang tidak boleh kosong.")
        return

    for barang_item in barang:
        if barang_item["kode"] == kode:
            print(f"Kode barang {kode} sudah terpakai untuk {barang_item['nama']}. Silakan masukkan kode baru.")
            return
        
    nama = input("Masukkan nama barang: ")
    if not nama:
        print("Nama barang tidak boleh kosong.")
        return
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    
    try:
        harga = float(input("Masukkan harga per unit: "))
        if harga <= 0:
            print("Lu mau jualan atau giveaway? Harus di atas 0.")
            return
    except ValueError:
        print("Harga harus berupa angka.")
        return
    
    barang.append({"kode": kode, "nama": nama, "jumlah": jumlah, "harga": harga})
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    for barang_item in barang:
        if barang_item["kode"] == kode:
            barang.remove(barang_item)
            print("Barang berhasil dihapus.")
            return
        else:
            print("Barang tidak ditemukan.")

def tampilkan_barang():
    if not barang:
        print("Tidak ada data barang.")
    else:
        print("\nDaftar Barang:")
        for barang_item in barang:
            print(f"Kode: {barang_item['kode']}, Nama: {barang_item['nama']}, Jumlah: {barang_item['jumlah']}, Harga: Rp{barang_item['harga']}")

def cari_barang():
    cari = input("Cari berdasarkan (1) kode atau (2) nama: ")
    
    if cari == '1':
        cari = input("Masukkan kode barang: ")
        hasil = [barang_item for barang_item in barang if cari == barang_item["kode"]]
    elif cari == '2':
        cari = input("Masukkan nama barang: ")
        hasil = [barang_item for barang_item in barang if cari == barang_item["nama"]]
    else:
        print("Pilihan tidak valid.")
        return

    if hasil:
        print("Hasil Pencarian:")
        for barang_item in hasil:
            print(f"Kode: {barang_item['kode']}, Nama: {barang_item['nama']}, Jumlah: {barang_item['jumlah']}, Harga: Rp{barang_item['harga']}")
    else:
        print("Barang tidak ditemukan.")

def update_barang():
    kode = input("Masukkan kode barang yang akan diubah: ")
    for barang_item in barang:
        if barang_item["kode"] == kode:
            print("Data barang saat ini:")
            print(f"Nama: {barang_item['nama']}, Jumlah: {barang_item['jumlah']}, Harga: Rp{barang_item['harga']}")
            jumlah_baru = input("Masukkan jumlah baru (kosongkan jika tidak ingin mengubah): ")
            harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
            if jumlah_baru:
                try:
                    barang_item["jumlah"] = int(jumlah_baru)
                except ValueError:
                    print("Jumlah harus berupa angka.")
                    return
                
            if harga_baru:
                try:
                    harga_baru_float = float(harga_baru)
                    if harga_baru_float <= 0:
                        print("Lu mau jualan atau giveaway? Harus di atas 0.")
                        return
                    barang_item["harga"] = harga_baru_float
                except ValueError:
                    print("Harga harus berupa angka.")
                    return

            print("Data barang berhasil diperbarui.")
            return
    print("Barang tidak ditemukan.")

menu()