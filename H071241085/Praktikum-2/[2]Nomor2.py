usia = int(input('Masukkan usia : '))
anggota = input('Apakah anda anggota (ya/tidak)? : ')

if usia < 5:
    harga = 'Gratis'
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

harga_diskon = f'Rp{harga * 0.8}' if anggota == 'ya' else f'Rp{harga}'
print (harga_diskon)



# ya,tidak = 'ya','tidak'
# remaja,dewasa,jompo = 50000,100000,70000

# if usia <= 5:
#     print('Gratis')
# elif usia > 5 or usia == 12:
#     print('Rp50.000')
# elif usia >= 13 or usia == 59:
#     print('Rp100.000')
# else:
#     print('Rp70.000')

# diskon = (remaja % 20) if 'ya' else 'Rp50.000' \
    #     (dewasa % 20) if 'ya' else 'Rp100.000' \
    # (jompo % 20) if 'ya' else 'Rp70.000'



