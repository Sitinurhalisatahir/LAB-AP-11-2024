total_harga = int(input('Masukkan total harga : '))
uang_diberikan = int(input('Masukkan uang yg diberika : '))

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

kembalian = uang_diberikan - total_harga
# print(kembalian)

for uang in pecahan_uang:
    if uang_diberikan < total_harga:
        print('uang kurang')
        break

    lembar = kembalian // uang
    if lembar > 0:
        print(f'{lembar} lembar Rp {uang:,}')
    kembalian %= uang