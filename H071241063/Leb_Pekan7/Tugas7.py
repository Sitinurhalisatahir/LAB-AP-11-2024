import os
import datetime

class SistemBioskop:
    def __init__(self):
        self.films = {}
        self.tickets = {}
        self.next_film_id = 1
        self.tickets_folder = "tickets"
        
        # Buat folder tickets jika belum ada
        if not os.path.exists(self.tickets_folder):
            os.makedirs(self.tickets_folder)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def tampilkan_menu_utama(self):
        while True:
            self.clear_screen()
            print("--- Sistem Pemesanan Tiket Bioskop ---")
            print("1. Admin")
            print("2. Pengunjung")
            print("3. Keluar")
            pilihan = input("Pilih peran (1/2/3): ")

            if pilihan == "1":
                self.menu_admin()
            elif pilihan == "2":
                self.menu_pengunjung()
            elif pilihan == "3":
                print("\nTerima kasih telah menggunakan sistem ini.")
                break

    def menu_admin(self):
        while True:
            self.clear_screen()
            print("--- Menu Admin ---")
            print("1. Tambah film")
            print("2. Hapus film")
            print("3. Daftar Tiket")
            print("4. Kembali")
            pilihan = input("Pilih opsi (1/2/3/4): ")

            if pilihan == "1":
                self.tambah_film()
            elif pilihan == "2":
                self.hapus_film()
            elif pilihan == "3":
                self.menu_daftar_tiket()
            elif pilihan == "4":
                break

    def menu_pengunjung(self):
        while True:
            self.clear_screen()
            print("--- Menu Pengunjung ---")
            print("1. Lihat daftar film")
            print("2. Beli tiket")
            print("3. Kembali")
            pilihan = input("Pilih opsi (1/2/3): ")

            if pilihan == "1":
                self.lihat_daftar_film()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "2":
                self.beli_tiket()
            elif pilihan == "3":
                break

    def tambah_film(self):
        self.clear_screen()
        print("--- Tambah Film ---")
        nama_film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        
        if nama_film:
            self.films[self.next_film_id] = nama_film
            print(f"\nFilm '{nama_film}' berhasil ditambahkan.")
            self.next_film_id += 1
            input("\nTekan Enter untuk kembali...")

    def hapus_film(self):
        while True:
            self.clear_screen()
            print("--- Hapus Film ---")
            print("Daftar Film:")
            if not self.films:
                print("0. Kembali")
                input("\nTekan Enter untuk kembali...")
                break
            
            for id_film, nama_film in self.films.items():
                print(f"{id_film}. {nama_film}")
            print("0. Kembali")

            pilihan = input("\nMasukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
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
        while True:
            self.clear_screen()
            print("--- Daftar Tiket ---")
            print("1. Lihat Daftar Tiket")
            print("2. Lihat Detail Tiket")
            print("3. Hapus Tiket")
            print("4. Kembali")
            pilihan = input("Pilih opsi (1/2/3/4): ")

            if pilihan == "1":
                self.lihat_daftar_tiket()
            elif pilihan == "2":
                self.lihat_detail_tiket()
            elif pilihan == "3":
                self.hapus_tiket()
            elif pilihan == "4":
                break

    def lihat_daftar_film(self):
        self.clear_screen()
        print("Daftar Film:")
        if not self.films:
            print("Tidak ada film tersedia")
            return
        
        for id_film, nama_film in self.films.items():
            print(f"{id_film}. {nama_film}")
        print("0. Kembali")

    def generate_ticket_id(self):
        now = datetime.datetime.now()
        return f"TICK{now.strftime('%d%m%Y%H%M%S')}"

    def beli_tiket(self):
        self.clear_screen()
        self.lihat_daftar_film()
        if not self.films:
            input("\nTekan Enter untuk kembali...")
            return

        pilihan = input("\nPilih nomor film yang ingin ditonton (atau 0 untuk kembali): ")
        
        try:
            id_film = int(pilihan)
            if id_film in self.films:
                ticket_id = self.generate_ticket_id()
                self.tickets[ticket_id] = {
                    'film_id': id_film,
                    'tanggal': datetime.datetime.now()
                }
                
                # Buat file tiket
                ticket_path = f"{self.tickets_folder}/{ticket_id}.txt"
                self.save_ticket_to_file(ticket_id, ticket_path)
                
                print(f"\nTiket berhasil dibeli. ID tiket Anda: {ticket_id}")
                print(f"File tiket telah dibuat: {ticket_path}")
                input("\nTekan Enter untuk kembali...")
        except ValueError:
            pass

    def save_ticket_to_file(self, ticket_id, ticket_path):
        ticket = self.tickets[ticket_id]
        film = self.films[ticket['film_id']]
        tanggal = ticket['tanggal'].strftime('%d-%m-%Y %H:%M:%S')
        
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
        self.clear_screen()
        print("Daftar Tiket:")
        if not self.tickets:
            print("Tidak ada tiket")
            input("\nTekan Enter untuk kembali...")
            return
        
        for ticket_id in self.tickets:
            print(f"1. {ticket_id}")
        input("\nTekan Enter untuk kembali...")

    def lihat_detail_tiket(self):
        while True:
            self.clear_screen()
            print("--- Detail Tiket ---")
            print("Daftar Tiket:")
            if not self.tickets:
                print("Tidak ada tiket")
                input("\nTekan Enter untuk kembali...")
                break
            
            for ticket_id in self.tickets:
                print(f"1. {ticket_id}")
            print("0. Kembali")

            pilihan = input("\nPilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
            try:
                selected_ticket = list(self.tickets.keys())[int(pilihan)-1]
                ticket = self.tickets[selected_ticket]
                film = self.films[ticket['film_id']]
                tanggal = ticket['tanggal'].strftime('%d-%m-%Y %H:%M:%S')
                
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
        while True:
            self.clear_screen()
            print("--- Hapus Tiket ---")
            print("Daftar Tiket:")
            if not self.tickets:
                print("Tidak ada tiket")
                input("\nTekan Enter untuk kembali...")
                break
            
            for ticket_id in self.tickets:
                print(f"1. {ticket_id}")
            print("0. Kembali")

            pilihan = input("\nPilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): ")
            
            if pilihan == "0":
                break
            
            try:
                selected_ticket = list(self.tickets.keys())[int(pilihan)-1]
                del self.tickets[selected_ticket]
                # Hapus file tiket jika ada
                ticket_path = f"{self.tickets_folder}/{selected_ticket}.txt"
                if os.path.exists(ticket_path):
                    os.remove(ticket_path)
                print(f"\nTiket '{selected_ticket}' berhasil dihapus.")
                input("\nTekan Enter untuk kembali...")
                break
            except (ValueError, IndexError):
                continue

if __name__ == "__main__":
    sistem = SistemBioskop()
    sistem.tampilkan_menu_utama()