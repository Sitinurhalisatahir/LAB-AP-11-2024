def get_inventory():
    return {}

def tambah_barang(inventory):
    kode_barang = input('masukkan kode barang: ')
    if kode_barang in inventory:
        print(f'{kode_barang} sudah ada. Gunakan fitur update untuk mengubah data')
    else:
        try:
            nama_barang = input('masukkan nama barang: ')
            jumlah_barang = int(input('masukkan jumlah barang: '))
            harga_barang = int(input('masukkkan harga per unit: '))
            inventory[kode_barang] = {
                'kode': kode_barang,
                'nama': nama_barang,
                'jumlah': jumlah_barang,
                'harga': harga_barang
            }
            print('barang berhasil ditambahkan')
        except ValueError:
            print('input tidak valid')

def hapus_barang(inventory):
    item = input('masukkan nama barang yg ingin dihapus: ')
    if item in inventory:
        del inventory[item]
        print('barang berhasil dihapus')
    else:
        print('barang tidak ditemukan')

def tampilkan_barang(inventory):
    if not inventory:
        print('barang tidak ada')
    else:
        print('===daftar barang===')
        for kode, data in inventory.items():
            print(f'kode: {data['kode']},'
                  f'nama: {data['nama']},'
                  f'jumlah: {data['jumlah']},'
                  f'harga: {data['harga']:}')

def cari_barang(inventory):
    item = input('cari berdasarkan (1) kode atau (2) nama: ')

    if item not in ['1','2']:
        print('pilih 1 atau 2 terlebih dahulu')
        return

    elif item == '1':
        kode_barang = input('masukkan kode barang: ')
        for nama, data in inventory.items():
            if data['kode'] == kode_barang:
                print(f'kode: {data['kode']},'
                      f'nama: {data['nama']},'
                      f'jumlah: {data['jumlah']},'
                      f'harga: {data['harga']}')
                return
        print('barang tidak ditemukan')

    elif item == '2':
        nama_barang = input('masukkan nama barang: ').lower()
        if nama_barang in inventory:
            data = inventory[nama_barang]
            print(f'kode: {data['kode']},'
                  f'nama: {data['nama']},'
                  f'jumlah: {data['jumlah']},'
                  f'harga: {data['harga']:.2f}')
        else:
            print('barang tidak ada')

def update_barang(inventory):
    kode_barang = input('masukkan kode barang yg ingin di update: ')

    if kode_barang in inventory:
        # try:
        nama_baru = input('masukkan nama baru: ')
        jumlah_baru = int(input('masukkan jumlah baru: '))
        harga_baru = int(input('masukkan harga baru: '))
        inventory[kode_barang] = {
            'kode': kode_barang,
            'nama': nama_baru,
            'jumlah': jumlah_baru,
            'harga': harga_baru
        }
        print('barang berhasil diupdate.')
        # except ValueError:
        #     print('input invalid, pastikan inputan berupa angka')
    else:
        print('barang tidak ditemukan')

def display_menu():
    inventory = get_inventory()
    while True:
        print('\n~~= Menu Inventory Barang =~~\n'
              '1. tambah barang\n'
              '2. hapus barang\n'
              '3. tampilkan inventory\n'
              '4. cari barang\n'
              '5. update barang\n'
              '6. keluar')

        pilihan = input('pilih menu (1-6): ')

        if pilihan == '1':
            tambah_barang(inventory)
        elif pilihan == '2':
            hapus_barang(inventory)
        elif pilihan == '3':
            tampilkan_barang(inventory)
        elif pilihan == '4':
            cari_barang(inventory)
        elif pilihan == '5':
            update_barang(inventory)
        elif pilihan == '6':
            break
        else:
            print('pilihan invalid')

if __name__ == '__main__':
    display_menu()