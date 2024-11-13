import os
from datetime import datetime

file_name = "daftar_film.txt"
folder_tiket = "folder_tiket"

os.makedirs(folder_tiket, exist_ok=True)

def menu_utama():
    while True:
        print(3 * "-", "Sistem Pemesanan Tiket Bioskop", 3 * "-")
        A = ["1. Admin", "2. Pengunjung", "3. Keluar"]
        for i in A:
            print(i)

        peran = input("Pilih peran (1/2/3): ")
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Terima kasih telah menggunakan sistem pemesanan tiket bioskop!")
            break
        else:
            print("Opsi tidak valid, silakan pilih kembali.")

def menu_admin():
    while True:
        print(3 * "-", "Menu Admin", 3 * "-")
        A = ["1. Tambah film", "2. Hapus film", "3. Tampilkan Film", "4. Daftar Tiket", "5. Kembali"]
        for j in A:
            print(j)
        opsi = input("Pilih opsi (1/2/3/4/5): ")

        if opsi == "1":
            tambah_film()
        elif opsi == "2":
            hapus_film()
        elif opsi == "3":
            tampilkan_film()  
        elif opsi == "4":
            daftar_tiket()
        elif opsi == "5":
            break
        else:
            print("Input tidak valid.")

def tambah_film():
    print(3 * "-", "Tambah Film", 3 * "-")
    film = input("Masukkan nama film yang ingin ditambahkan (atau tekan enter untuk kembali): ")
    if film: 
        with open(file_name, "a") as file:
            file.write(film + "\n")
        print(f"Film '{film}' ditambahkan ke file {file_name}.")
    else:
        print("Input film kosong, kembali ke menu.")

def hapus_film():
    print(3 * "-", "Hapus Film", 3 * "-")
    print("Daftar Film:")
    
    with open(file_name, "r") as file:
        nama_film = file.readlines()  # Membuat list dari file daftar film
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")

    try:
        nomor_baris = int(input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): "))
        if nomor_baris == 0:
            print("Kembali ke menu.")
            return
        if 1 <= nomor_baris <= len(nama_film):
            del nama_film[nomor_baris - 1]

            with open(file_name, "w") as file:
                file.writelines(nama_film)
            print("Film telah dihapus dari daftar.")
        else:
            print("Nomor baris tidak valid.")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def tampilkan_film():
    print(3 * "-", "Tampilkan Film", 3 * "-")
    print("Daftar Film:")
    with open(file_name, "r") as file:
        nama_film = file.readlines()
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")

    print("Film telah ditampilkan.")

def daftar_tiket():
    while True:
        print(3 * "-", "Daftar Tiket", 3 * "-")
        B = ["1. Lihat Daftar Tiket", "2. Lihat Detail Tiket", "3. Hapus Tiket", "4. Kembali"]
        for a in B:
            print(a)
        opsi = input("Pilih opsi (1/2/3/4): ")

        if opsi == "1":
            lihat_daftar_tiket()
        elif opsi == "2":
            lihat_detail_tiket()
        elif opsi == "3":
            hapus_tiket()
        elif opsi == "4":
            break
        else:
            print("Input tidak valid.")

def lihat_daftar_tiket():
    print("Daftar tiket:")
    try:
        tiket_files = os.listdir(folder_tiket)          #membuat list berdasarkan nama file yang ada di folder
        
        if not tiket_files:
            print("Tidak ada tiket yang tersedia.")
        else:
            for index, id_tiket in enumerate(tiket_files, start=1):
                print(f"{index}. {id_tiket}")
    except Exception as e:
        print(f"Error! Tidak dapat membaca daftar tiket: {e}")

def lihat_detail_tiket():
    try:
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dilihat detailnya: "))
        file_tiket = os.listdir(folder_tiket)  # Membuat list berdasarkan nama file yang ada di folder
        
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            with open(tiket_file_path, "r") as file:
                detail_tiket = file.read()
            print(f"Detail Tiket:\n{detail_tiket}")
        else:
            print(f"Tiket dengan nomor tiket {nomor_tiket} tidak ditemukan.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def hapus_tiket():
    try:
        nomor_tiket = int(input("Masukkan nomor tiket yang ingin dihapus: "))
        file_tiket = os.listdir(folder_tiket)
        
        if nomor_tiket == 0:
            print("Kembali ke menu.")
            return
        if 1 <= nomor_tiket <= len(file_tiket):
            tiket_file_path = os.path.join(folder_tiket, file_tiket[nomor_tiket - 1])
            os.remove(tiket_file_path)
            print(f"Tiket nomor {nomor_tiket} telah dihapus.")
        else:
            print("Nomor tiket tidak valid.")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor tiket.")

def menu_pengunjung():
    while True:
        print(3 * "-", "Menu Pengunjung", 3 * "-")
        C = ["1. Lihat daftar film", "2. Beli tiket", "3. Kembali"]
        for j in C:
            print(j)
        opsi = input("Pilih opsi (1/2/3): ")

        if opsi == "1":
            daftar_film()
        elif opsi == "2":
            beli_tiket()
        elif opsi == "3":
            break
        else:
            print("Input tidak valid.")
    
def daftar_film():
    print("Daftar film:")
    try:
        with open(file_name, "r") as file:
            nama_film = file.readlines()
        
        for index, line in enumerate(nama_film, start=1):
            print(f"{index}. {line.strip()}")

    except Exception as e:
        print(f"Error! Daftar film tidak ditemukan: {e}")

def beli_tiket():
    print("Daftar film:")
    with open(file_name, "r") as file:
        nama_film = file.readlines()
    
    for index, line in enumerate(nama_film, start=1):
        print(f"{index}. {line.strip()}")
    print("0. Kembali")

    try:
        nomor_film = int(input("Pilih nomor film yang ingin ditonton (atau 0 untuk kembali): "))
        if nomor_film == 0:
            return
        if 1 <= nomor_film <= len(nama_film):
            film = nama_film[nomor_film - 1]
            tiket_id = buat_tiket()
            tiket_info = detail_tiket(film, tiket_id)
            simpan_tiket(tiket_info, tiket_id)
            print(f"Tiket berhasil dibuat dengan ID: {tiket_id}")
        else:
            print(f"Nomor film {nomor_film} tidak ditemukan")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor film.")

def buat_tiket():
    now = datetime.now()
    tiket_id = now.strftime("TICK%d%m%Y%H%M%S") + "!" #format penulisan tiket sesuai objek datetime
    return tiket_id

def detail_tiket(film, tiket_id):
    detail = f"""
    +-----------------------------------+
    |        TIKET BIOSKOP              |
    | ID TICKET: {tiket_id}             |
    | Film: {film}                      |
    | Tanggal: {datetime.now()}         |
    +-----------------------------------+
    |     Terimakasih telah membeli     |
    |            tiket anda             |
    +-----------------------------------+
    """
    return detail

def simpan_tiket(tiket_info, tiket_id):
    
    try:
        tiket_file_path = os.path.join(folder_tiket, f"{tiket_id}.txt")
        with open(tiket_file_path, "w") as file:
            file.write(tiket_info)
        print(f"Tiket disimpan di {tiket_file_path}.")
    except Exception as e:
        print(f"Error! Tidak dapat menyimpan tiket: {e}")

menu_utama()    