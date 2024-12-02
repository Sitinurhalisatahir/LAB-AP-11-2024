import datetime
import os

### Function admin
def buat_folder(nama_folder):
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)

def tambah_film(nama_film):
    with open('daftar_film.txt', 'a') as file:
        file.write(nama_film + '\n')
    print(f'film {nama_film} berhasil ditambahkan.')

## Bisa di panggil di menu admin dan customer
def tampilkan_daftar_film():
    try:
        with open('daftar_film.txt', 'r') as file:
            data_film = file.readlines()
        print('Daftar film:')
        for i, film in enumerate(data_film, 1):
            print(f'{i}. {film.strip()}')
    except FileNotFoundError:
        print('Belum ada film yg ditambahkan')

def hapus_film(nama_film):
    with open('daftar_film.txt', 'r') as file:
        data_film = file.readlines()
    for film in data_film:
        if film.strip() == nama_film:
            data_film.remove(film)
            break
    else:
        print(f'judul {nama_film} tidak ditemukan')
    with open('daftar_film.txt', 'w') as file:
        file.writelines(data_film)
    print(f'film {nama_film} berhasil dihapus')

### Function Customer
def beli_tiket(judul_film):
    id_tiket = f'TICK{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}'
    with open('tiket.txt', 'a') as file:
        file.write((f"""
        +--------------------------------+
        |          TIKET BIOSKOP         |
        +--------------------------------+
        | ID Tiket : {id_tiket}          
        | Film     : {judul_film}        
        | Tanggal  : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        +--------------------------------+
        |  Terima kasih telah membeli    |
        |        tiket Film ini!         |
        +--------------------------------+
        """))
    with open(f'tiket/{id_tiket}.txt', 'w') as file:
        file.write((f"""
        +--------------------------------+
        |          TIKET BIOSKOP         |
        +--------------------------------+
        | ID Tiket : {id_tiket}          
        | Film     : {judul_film}        
        | Tanggal  : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        +--------------------------------+
        |  Terima kasih telah membeli    |
        |        tiket Film ini!         |
        +--------------------------------+
        """))
        print(f"\nTiket untuk film '{judul_film}' berhasil dibeli. ID Tiket: {id_tiket}")
        return id_tiket

def tampilkan_tiket():
    try:
        folder_tiket = 'tiket/'
        file_tiket = os.listdir(folder_tiket)
        print('Daftar tiket:')
        for file in file_tiket:
            with open(folder_tiket + file, 'r') as f:
                tiket = f.read()
                print(tiket)
    except FileNotFoundError:
        print('Belum ada tiket yang dibeli.')

### Function Main Menu
def menu_utama():
    while True:
        print('\n=== menu utama ===\n'
              '1. Admin\n'
              '2. Pengunjung\n'
              '3. keluar')
        pilihan = input('pilih role (1-3): ')

        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        elif pilihan == '3':
            print('Terima kasih telah berkunjung\n'
                  'sampai jumpa lagi.')
            break
        else:
            print('invalid')

def menu_admin():
    while True:
        print('\n=== menu admin ===\n'
              '1. tambah film\n'
              '2. hapus film\n'
              '3. tampilkan daftar film\n'
              '4. manajemen tiket\n'
              '5. kembali (menu utama)')
        pilihan = input('pilih menu (1-5): ')

        if pilihan == '1':
            while True:
                print('\n=== tambah film ===')
                judul = input('masukkan judul film yg ingin ditambahkan\n'
                              '(enter utk kembali): ')
                if judul:
                    tambah_film(judul)
                else:
                    print('kembali ke menu admin.')
                    break
        elif pilihan == '2':
            while True:
                print('\n=== hapus film ==='
                      'daftar film:\n')
                with open('daftar_film.txt', 'r') as file:
                    data_film = file.readlines()
                    for i, film in enumerate(data_film, start=1):
                        print(f'{i}. {film.strip()}')
                print('0. kembali.')

                nomor_film = input('masukkan nomor film yg ingin dihapus\n'
                                   '(0. utk kembali): ')
                if nomor_film == '0':
                    print('\nkembali ke menu admin.')
                    break
                else:
                    try:
                        nomor_film = int(nomor_film)
                        if 1 <= nomor_film <= len(data_film):
                            judul = data_film[nomor_film - 1].strip()
                            hapus_film(judul)
                        else:
                            print('nomor film tidak valid.')
                    except ValueError:
                        print('nomor film harus berupa angka.')
        elif pilihan == '3':
            tampilkan_daftar_film()
        elif pilihan == '4':
            menu_daftar_tiket()
        elif pilihan == '5':
            print('\nKembali ke menu utama.')
            break
        else:
            print('pilihan tidak valid.')

## For ticket management
def menu_daftar_tiket():
    while True:
        print('\n=== daftar tiket ===\n'
              '1. lihat daftar tiket\n'
              '2. lihat detail tiket\n'
              '3. hapus tiket\n'
              '4. kembali')
        pilihan = input('pilih menu (1-4): ')

        if pilihan == '1':
            try:
                folder_tiket = 'tiket/'
                file_tiket = os.listdir(folder_tiket)
                print('\nDaftar tiket:')
                for i, file in enumerate(file_tiket, start=1):
                    print(f'{i}.{file.replace('.txt', '')}')
            except FileNotFoundError:
                print('belum ada tiket yg dibeli.')
        elif pilihan == '2':
            folder_tiket = 'tiket/'
            file_tiket = os.listdir(folder_tiket)
            print('\n=== detail tiket ===')
            for i, file in enumerate(file_tiket, start=1):
                print(f'{i}.{file.replace('.txt','')}')
            print('0. kembali')
            while True:
                pilihan_tiket = input('\nPilih nomor tiket yg ingin dilihat (0 utk kembali): ')
                if pilihan_tiket == '0':
                    print('\nKembali ke daftar tiket.')
                    break
                else:
                    try:
                        file_tiket = file_tiket[int(pilihan_tiket) - 1]
                        with open(folder_tiket + file_tiket, 'r')as f:
                            detail_tiket = f.read()
                            print(f'\nDetail tiket "{file_tiket.replace('.txt', '')}":')
                            print(detail_tiket)
                            break
                    except (IndexError, ValueError):
                        print('pilihan tidak valid. silahkan coba lagi.')
        elif pilihan == '3':
            folder_tiket = 'tiket/'
            file_tiket = os.listdir(folder_tiket)
            print('\n=== hapus tiket ===')
            for i, file in enumerate(file_tiket, start=1):
                print(f'{i}.{file.replace('.txt', '')}')
            print('0. kembali')
            while True:
                hapus_pilihan = input('\nPilih nomor tiket yg ingin dihapus (0 utk kembali): ')
                if pilihan == '0':
                    print('\nKembali ke daftar tiket.')
                    break
                else:
                    try:
                        file_tiket = file_tiket[int(hapus_pilihan) - 1]
                        os.remove(folder_tiket + file_tiket)
                        print(f'\nTiket "{file_tiket.replace('.txt', '')}" telah dihapus.')
                        break
                    except (IndexError, ValueError):
                        print('pilihan tidak valid. Coba lagi.')
        elif pilihan == '4':
            print('\nKembali ke menu admin.')
            break
        else:
            print('pilihan tidak valid.')

def menu_pengunjung():
    while True:
        print('\n=== Menu Pengunjung ===\n'
              '1.lihat daftar film\n'
              '2.beli tiket\n'
              '3.kembali (menu utama)')
        pilihan = input('pilih menu (1-3): ')

        if pilihan == '1':
            tampilkan_daftar_film()
        elif pilihan == '2':
            print('\n=== pembelian tiket ===\n'
                  '\nDaftar film:')
            with open('daftar_film.txt', 'r') as file:
                data_film = file.readlines()
            for i, film in enumerate(data_film, start=1):
                print(f'{i}. {film.strip()}')
            print('0.Kembali')
            while True:
                nomor_film = input('\npilih nomor film yg ingin ditonton (0 utk kembali): ')
                if nomor_film == '0':
                    break
                else:
                    try:
                        nomor_film = int(nomor_film)
                        if 1 <= nomor_film <= len(data_film):
                            judul = data_film[nomor_film - 1].strip()
                            id_tiket = beli_tiket(judul)
                            print(f'file tiket telah dibuat: tiket/{id_tiket}.txt')
                            break
                        else:
                            print('nomor filmm tidak valid.')
                    except ValueError:
                        print('nomor file harus berupa angka.')
        elif pilihan == '3':
            print('\nKembali ke Menu utama.')
            break
        else:
            print('pilihan tidak valid.')

## Make sure folder yg diperlukan ada
buat_folder('data')
buat_folder('tiket')
if not os.path.exists('daftar_film.txt'):
    open('daftar_film.txt', 'w').close()
if not os.path.exists('tiket.txt'):
    open('tiket.txt', 'w').close()

if __name__ == '__main__':
    menu_utama()