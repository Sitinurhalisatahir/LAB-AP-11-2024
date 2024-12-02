harga = int(input('Masukkan total harga: '))
uang_pelanggan = int(input('Masukkan uang yang diberikan: '))

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

kembalian = uang_pelanggan - harga

if kembalian > 0:
    print(f'Kembalian anda adalah {kembalian}')
else:
    print('Uang anda tidak cukup')

print('Lembar kembalian: ')

for pecahan in pecahan_uang:
    lembaran = kembalian // pecahan
    kembalian %= pecahan
    if lembaran > 0:
        print(f'{lembaran} Lembar {pecahan}')