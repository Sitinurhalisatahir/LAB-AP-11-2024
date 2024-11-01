import os
import datetime

class SistemBioskop:
    """
    Kelas utama untuk sistem manajemen bioskop.
    Menangani pemesanan tiket, manajemen film, dan administrasi sistem.
    """
    def __init__(self):
        # Inisialisasi dictionary untuk menyimpan data film dan tiket
        self.films = {}          # Format: {id_film: nama_film}
        self.tickets = {}        # Format: {ticket_id: {film_id, tanggal}}
        self.next_film_id = 1    # ID untuk film berikutnya yang akan ditambahkan
        self.tickets_folder = "tickets"  # Folder untuk menyimpan file tiket
        
        # Membuat folder tickets jika belum ada
        if not os.path.exists(self.tickets_folder):
            os.makedirs(self.tickets_folder)

    def clear_screen(self):
        """Membersihkan layar terminal untuk tampilan yang lebih rapi"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Mendukung Windows dan Unix

    def tampilkan_menu_utama(self):
        """
        Menampilkan menu utama dengan pilihan peran Admin atau Pengunjung.
        Loop utama program yang mengarahkan ke submenu berdasarkan pilihan pengguna.
        """
        while True:
            self.clear_screen()
            print("--- Sistem Pemesanan Tiket Bioskop ---")
            print("1. Admin")
            print("2. Pengunjung")
            print("3. Keluar")
            pilihan = input("Pilih peran (1/2/3): ")

            # Routing ke menu yang sesuai
            if pilihan == "1":
                self.menu_admin()
            elif pilihan == "2":
                self.menu_pengunjung()
            elif pilihan == "3":
                print("\nTerima kasih telah menggunakan sistem ini.")
                break

    def menu_admin(self):
        """
        Menu khusus untuk admin dengan akses ke fungsi manajemen sistem.
        Termasuk: tambah/hapus film dan manajemen tiket.
        """
        while True:
            self.clear_screen()
            print("--- Menu Admin ---")
            print("1. Tambah film")
            print("2. Hapus film")
            print("3. Daftar Tiket")
            print("4. Kembali")
            pilihan = input("Pilih opsi (1/2/3/4): ")

            # Routing ke fungsi admin yang sesuai
            if pilihan == "1":
                self.tambah_film()
            elif pilihan == "2":
                self.hapus_film()
            elif pilihan == "3":
                self.menu_daftar_tiket()
            elif pilihan == "4":
                break

    def menu_pengunjung(self):
        """
        Menu untuk pengunjung bioskop.
        Menyediakan akses ke daftar film dan pembelian tiket.
        """
        while True:
            self.clear_screen()
            print("--- Menu Pengunjung ---")
            print("1. Lihat daftar film")
            print("2. Beli tiket")
            print("3. Kembali")
            pilihan = input("Pilih opsi (1/2/3): ")

            # Routing ke fungsi pengunjung yang sesuai
            if pilihan == "1":
                self.lihat_daftar_film()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "2":
                self.beli_tiket()
            elif pilihan == "3":
                break

    def tambah_film(self):
        """
        Fungsi untuk menambahkan film baru ke sistem.
        Film disimpan dengan ID unik yang bertambah secara otomatis.
        """
        self.clear_screen()
        print("--- Tambah Film ---")
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        
        if nama_film:
            # Menambahkan film baru ke dictionary
            self.films[self.next_film_id] = nama_film
            print(f"\nFilm '{nama_film}' berhasil ditambahkan.")
            self.next_film_id += 1
            input("\nTekan Enter untuk kembali...")

    def hapus_film(self):
        """
        Fungsi untuk menghapus film dari sistem.
        Menampilkan daftar film yang tersedia dan memungkinkan admin untuk memilih yang akan dihapus.
        """
        while True:
            self.clear_screen()
            print("--- Hapus Film ---")
            print("Daftar Film:")
            if not self.films:
                print("0. Kembali")
                input("\nTekan Enter untuk kembali...")
                break
            
            # Menampilkan daftar film yang tersedia
            for id_film, nama_film in self.films.items():
                print(f"{id_film}. {nama_film}")
            print("0. Kembali")

            pilihan = input("\nMasukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
            # Proses penghapusan film
            try:
                id_film = int(pilihan)
                if id_film in self.films:
                    nama_film = self.films[id_film]
                    del self.films[id_film]
                    print(f"\nFilm '{nama_film}' berhasil dihapus.")
                    input("\nTekan Enter untuk kembali...")
                    break
            except ValueError:
                continue

    def menu_daftar_tiket(self):
        """
        Menu untuk manajemen tiket.
        Menyediakan akses ke fungsi-fungsi terkait tiket seperti melihat dan menghapus tiket.
        """
        while True:
            self.clear_screen()
            print("--- Daftar Tiket ---")
            print("1. Lihat Daftar Tiket")
            print("2. Lihat Detail Tiket")
            print("3. Hapus Tiket")
            print("4. Kembali")
            pilihan = input("Pilih opsi (1/2/3/4): ")

            # Routing ke fungsi tiket yang sesuai
            if pilihan == "1":
                self.lihat_daftar_tiket()
            elif pilihan == "2":
                self.lihat_detail_tiket()
            elif pilihan == "3":
                self.hapus_tiket()
            elif pilihan == "4":
                break

    def lihat_daftar_film(self):
        """
        Menampilkan daftar film yang tersedia di sistem.
        """
        self.clear_screen()
        print("Daftar Film:")
        if not self.films:
            print("Tidak ada film tersedia")
            return
        
        # Menampilkan semua film yang tersedia
        for id_film, nama_film in self.films.items():
            print(f"{id_film}. {nama_film}")
        print("0. Kembali")

    def generate_ticket_id(self):
        """
        Menghasilkan ID tiket unik berdasarkan timestamp.
        Format: TICK + DDMMYYYYHHMMSS
        """
        now = datetime.datetime.now()
        return f"TICK{now.strftime('%d%m%Y%H%M%S')}"

    def beli_tiket(self):
        """
        Proses pembelian tiket.
        Mencakup pemilihan film dan pembuatan file tiket.
        """
        self.clear_screen()
        self.lihat_daftar_film()
        if not self.films:
            input("\nTekan Enter untuk kembali...")
            return

        pilihan = input("\nPilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")
        
        try:
            id_film = int(pilihan)
            if id_film in self.films:
                # Membuat tiket baru
                ticket_id = self.generate_ticket_id()
                self.tickets[ticket_id] = {
                    'film_id': id_film,
                    'tanggal': datetime.datetime.now()
                }
                
                # Menyimpan tiket ke file
                ticket_path = f"{self.tickets_folder}/{ticket_id}.txt"
                self.save_ticket_to_file(ticket_id, ticket_path)
                
                print(f"\nTiket berhasil dibeli. ID tiket Anda: {ticket_id}")
                print(f"File tiket telah dibuat: {ticket_path}")
                input("\nTekan Enter untuk kembali...")
        except ValueError:
            pass

    def save_ticket_to_file(self, ticket_id, ticket_path):
        """
        Menyimpan informasi tiket ke file dengan format yang rapi.
        
        Parameters:
            ticket_id (str): ID tiket yang akan disimpan
            ticket_path (str): Path file untuk menyimpan tiket
        """
        ticket = self.tickets[ticket_id]
        film = self.films[ticket['film_id']]
        tanggal = ticket['tanggal'].strftime('%d-%m-%Y %H:%M:%S')
        
        # Membuat file tiket dengan format yang rapi
        with open(ticket_path, 'w') as f:
            f.write("+" + "-" * 38 + "+\n")
            f.write("|" + " " * 14 + "TIKET BIOSKOP" + " " * 13 + "|\n")
            f.write("+" + "-" * 38 + "+\n")
            f.write(f"| ID Tiket : {ticket_id:<27} |\n")
            f.write(f"| Film     : {film:<27} |\n")
            f.write(f"| Tanggal  : {tanggal:<27} |\n")
            f.write("+" + "-" * 38 + "+\n")
            f.write("|" + " " * 6 + "Terima kasih telah membeli" + " " * 7 + "|\n")
            f.write("|" + " " * 12 + "tiket Anda!" + " " * 12 + "|\n")
            f.write("+" + "-" * 38 + "+\n")

    def lihat_daftar_tiket(self):
        """
        Menampilkan daftar semua tiket yang ada di sistem.
        """
        self.clear_screen()
        print("Daftar Tiket:")
        if not self.tickets:
            print("Tidak ada tiket")
            input("\nTekan Enter untuk kembali...")
            return
        
        # Menampilkan semua ID tiket
        for ticket_id in self.tickets:
            print(f"1. {ticket_id}")
        input("\nTekan Enter untuk kembali...")

    def lihat_detail_tiket(self):
        """
        Menampilkan detail lengkap dari tiket yang dipilih.
        """
        while True:
            self.clear_screen()
            print("--- Detail Tiket ---")
            print("Daftar Tiket:")
            if not self.tickets:
                print("Tidak ada tiket")
                input("\nTekan Enter untuk kembali...")
                break
            
            # Menampilkan daftar tiket yang tersedia
            for ticket_id in self.tickets:
                print(f"1. {ticket_id}")
            print("0. Kembali")

            pilihan = input("\nPilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
            try:
                # Menampilkan detail tiket yang dipilih
                selected_ticket = list(self.tickets.keys())[int(pilihan)-1]
                ticket = self.tickets[selected_ticket]
                film = self.films[ticket['film_id']]
                tanggal = ticket['tanggal'].strftime('%d-%m-%Y %H:%M:%S')
                
                # Menampilkan informasi tiket dengan format yang rapi
                print(f"\nDetail Tiket '{selected_ticket}':")
                print("+" + "-" * 38 + "+")
                print("|" + " " * 14 + "TIKET BIOSKOP" + " " * 13 + "|")
                print("+" + "-" * 38 + "+")
                print(f"| ID Tiket : {selected_ticket:<27} |")
                print(f"| Film     : {film:<27} |")
                print(f"| Tanggal  : {tanggal:<27} |")
                print("+" + "-" * 38 + "+")
                print("|" + " " * 6 + "Terima kasih telah membeli" + " " * 7 + "|")
                print("|" + " " * 12 + "tiket Anda!" + " " * 12 + "|")
                print("+" + "-" * 38 + "+")
                input("\nTekan Enter untuk kembali...")
                break
            except (ValueError, IndexError):
                continue

    def hapus_tiket(self):
        """
        Menghapus tiket dari sistem dan file terkait.
        """
        while True:
            self.clear_screen()
            print("--- Hapus Tiket ---")
            print("Daftar Tiket:")
            if not self.tickets:
                print("Tidak ada tiket")
                input("\nTekan Enter untuk kembali...")
                break
            
            # Menampilkan daftar tiket yang tersedia
            for ticket_id in self.tickets:
                print(f"1. {ticket_id}")
            print("0. Kembali")

            pilihan = input("\nPilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
            try:
                # Proses penghapusan tiket
                selected_ticket = list(self.tickets.keys())[int(pilihan)-1]
                del self.tickets[selected_ticket]
                # Menghapus file tiket jika ada
                ticket_path = f"{self.tickets_folder}/{selected_ticket}.txt"
                if os.path.exists(ticket_path):
                    os.remove(ticket_path)
                print(f"\nTiket '{selected_ticket}' berhasil dihapus.")
                input("\nTekan Enter untuk kembali...")
                break
            except (ValueError, IndexError):
                continue

# Entry point program
if __name__ == "__main__":
    sistem = SistemBioskop()
    sistem.tampilkan_menu_utama()