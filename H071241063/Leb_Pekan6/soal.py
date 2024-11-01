inventory = {}


#fungsi unutk menambahkan barang ke inventori
def tambah_barang():
    kode = input("Masukkan kode barang: ")
    nama = input("Masukan nama barang: ")
    jumlah = int(input("masukkan jumlah barang: "))
    harga = float(input("Masukkan harga per unit: "))

    inventory[kode] = {"nama": nama, "jumlah": jumlah, "harga": harga}
    print("Barang berhasil ditambahkan.")

#Fungsi untuk menghapus barang
def hapus_barang():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print("Barang berhasil dihapus")
    else: 
        print("Barang tidak diTemukan")

#Fungsi untuk menampilkan barang
def tampilkan_barang():
    if inventory: 
        for kode, barang in inventory.items():
            print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: {barang['harga']}")
    else:
        print("Inventori kosong.")

#fungsi untuk mencari barang berdasarkan kode dan nama
def cari_barang():
    print("Cari berdasarkan (1) Kode atau (2) Nama: ")
    pilihan = input()
    if pilihan == "1":
        kode = input("Masukkan kode barang: ")
        if kode in inventory:
            barang = inventory[kode]
            print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: {barang['harga']}")
        else: 
          print("Barang tidak di temukan.")
    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        found = False
        for kode, barang in inventory.items():
            if barang['nama'].lower() == nama.lower():
                print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: {barang['harga']}")
                found = True
        if not found:
            print("Barang Tidak ditemukan.")

#fungsi untuk update barang           
def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventory:
        jumlah_baru = int(input("Masukkan jumlah baru: "))
        harga_baru  = float(input("Masukkan harga per unit: "))
        inventory[kode]["jumlah"] = jumlah_baru
        inventory[kode]["harga"]  = harga_baru
        print("Data barang berhasil diperbarui.")
    else: 
        print("Barang tidak di temukan.")

#Fungsi untuk menampilkan menu utama
def menu():
    while True:
        print("\n==== Menu Inventori Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Kelaur")

        pilihan = input("Pilih opsi (1-6): ")

        if pilihan  == '1':
            tambah_barang()
        elif pilihan == '2':
            tambah_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima Kasih telah menggunakn program inventori.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memastikan bahwa fungsi menu hanya dijalankan jika script dijalankan secara langsung
if __name__ == "__main__":
    menu()


         