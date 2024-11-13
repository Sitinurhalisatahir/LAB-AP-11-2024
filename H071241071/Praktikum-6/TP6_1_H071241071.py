barang = []

def tambah_barang():
    kode = input("Masukkan kode barang: ")

    if kode == "":
            print("Kode barang tidak boleh kosong!!!")
            return

    for barang_item in barang:
        if barang_item["kode"] == kode:
            print(f"Kode barang sudah terpakai untuk {barang_item['nama']}")
            return

    nama = input("Masukkan nama barang: ")
    
    if nama == "":
        print("Nama barang tidak boleh kosong!!!")
        return
    
    try:
        jumlah = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Jumlah barang harus berupa angka.")
        return

    try:
        harga = float(input("Masukkan harga per unit: "))
        if harga < 0:
            print("Yakali harga negatif")
            return
    except ValueError:
        print("Harga harus berupa angka.")
        return
    
    inventory = {
        "kode": kode, 
        "nama": nama, 
        "jumlah": jumlah, 
        "harga": harga
 }
    barang.append(inventory)
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    for i in barang:
        if i["kode"] == kode:
            barang.remove(i)
            print("Barang berhasil dihapus.")
            return
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
    
    if cari == '1' :
        kode = input("Masukkan kode barang yang ingin dicari: ")
        for barang_item in barang:
            if barang_item['kode'] == kode:
                print(f"Barang ditemukan: Kode: {barang_item['kode']}, Nama: {barang_item['nama']}, Jumlah: {barang_item['jumlah']}, Harga: {barang_item['harga']}")
                break
            else:
                print(f"Barang dengan kode {kode} tidak ditemukan.")
    elif cari == '2' :    
        nama = input("Masukkan nama barang yang ingin dicari: ")
        for barang_item in barang:
            if barang_item['nama'] == nama:
                print(f"Barang ditemukan: Kode: {barang_item['kode']}, Nama: {barang_item['nama']}, Jumlah: {barang_item['jumlah']}, Harga: {barang_item['harga']}")
                break
            else:
                print(f"Barang dengan kode {nama} tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")
        return 

def update_barang():
    kode = input("Masukkan kode barang yang akan diubah: ")
    for i in barang:
        if i["kode"] == kode:
            print("Data barang saat ini:")
            print(f"Nama: {i['nama']}, Jumlah: {i['jumlah']}, Harga: Rp{i['harga']}")
            jumlah_baru = input("Masukkan jumlah baru (kosongkan jika tidak ingin mengubah): ")
            harga_baru = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
            if jumlah_baru:
                i["jumlah"] = int(jumlah_baru)
            if harga_baru:
                i["harga"] = float(harga_baru)
            print("Data barang berhasil diperbarui.")
            return
        else :
            print("Barang tidak ditemukan.")

def menu():
    while True:
        print("\n=== Menu Inventory Barang ===")
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

menu()