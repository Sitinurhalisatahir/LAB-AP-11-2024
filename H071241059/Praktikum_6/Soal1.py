inventory = []

def tambah_barang(inventory):
    while True:
        try:
            kode_barang = input("Masukkan kode barang: ")
            
            if not kode_barang.isdigit():
                print("Kode barang harus berupa angka")
                continue
            
            for barang in inventory:
                if barang["Kode"] == kode_barang:
                    print("Kode barang sudah ada")
                    break
            else: 
                nama_barang = input("Masukkan nama barang: ")
                for barang in inventory:
                    if barang["Nama"] == nama_barang:
                        print("Nama barang sudah ada")
                        break
                else: 
                    jumlah_barang = int(input("Masukkan jumlah barang: "))
                    harga_barang = int(input("Masukkan harga barang: "))
                    
                    inventory.append({
                        "Kode": kode_barang,
                        "Nama": nama_barang,
                        "Jumlah": jumlah_barang,
                        "Harga per unit": harga_barang
                    })
                    break  
        except ValueError:
            print("Input tidak valid, silakan coba lagi.")
    return "Barang berhasil ditambahkan"

def hapus_barang(inventory):
    try:
        kode = input("Masukkan kode barang yang akan dihapus: ")
        for barang in inventory:
            if barang["Kode"] == kode:
                inventory.remove(barang)
                return "Barang berhasil dihapus"
        print("Barang tidak ditemukan")
    except ValueError:
        print("input tidak valid")

def tampilkan_barang(inventory):
    if len(inventory) == 0:
        print("Inventory kosong")
    else:
        for barang in inventory:
            print(f"Kode: {barang['Kode']}, Nama: {barang['Nama']}, Jumlah: {barang["Jumlah"]}, Harga per unit: {barang["Harga per unit"]}")


def cari_barang(inventory):
    try:
        opsi = int(input("Cari berdasarkan (1) Kode atau (2) Nama: "))
        if opsi == 1:
            kode = input("Masukkan kode barang: ")
            for barang in inventory:
                if barang["Kode"] == kode:
                    print(f"Kode: {barang["Kode"]}, Nama: {barang["Nama"]}, Jumlah: {barang["Jumlah"]}, Harga per unit: {barang["Harga per unit"]}")
                    return
            print("Kode barang tidak ditemukan")
        elif opsi == 2:
            nama = input("Masukkan nama barang: ")
            for barang in inventory:
                if barang["Nama"] == nama:
                    print(f"Kode: {barang["Kode"]}, Nama: {barang["Nama"]}, Jumlah: {barang["Jumlah"]}, Harga per unit: {barang["Harga per unit"]}")
                    return
            print("Nama barang tidak ditemukan")
    except ValueError:
        print("Input tidak valid")

def update_barang(inventory):
    while True:
        try:
            kode = input("Masukkan kode barang yang ingin diupdate: ")
            if not kode.isdigit():
                    print("Kode barang harus berupa angka")
                    continue
            for barang in inventory:
                if barang["Kode"] == kode:
                    jumlah_baru = int(input("Masukkan jumlah baru: "))
                    harga_baru = int(input("Masukkan harga per unit baru: "))

                    barang["Jumlah"] = jumlah_baru
                    barang["Harga per unit"] = harga_baru
                    return "Barang telah di update"
            print("Barang tidak ditemukan")
        except ValueError:
            print("Masukkan angka valid")

while True:
    print("=== Menu Inventori Barang ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Barang")
    print("4. Cari Barang")
    print("5. Update Barang")
    print("6. Keluar")

    pilihan = int(input("Pilih opsi (1-6): "))

    if pilihan == 1:
        print(tambah_barang(inventory))
    elif pilihan == 2:
        print(hapus_barang(inventory))
    elif pilihan == 3:
        tampilkan_barang(inventory)
    elif pilihan == 4:
        cari_barang(inventory)
    elif pilihan == 5:
        print(update_barang(inventory))
    elif pilihan == 6:
        break