"""mengidentifikasi jenis segitiga"""
pertama = int(input('Masukkan panjang sisi pertama : '))
kedua = int(input('Masukkan panjang sisi kedua : '))
ketiga = int(input('Masukkan panjang sisi ketiga : '))


if pertama == kedua == ketiga > 0:
    if pertama == kedua == ketiga:
        print('segitiga sama sisi')
    elif pertama == kedua or kedua == ketiga or pertama == ketiga:
        print('segitiga sama kaki')
    else:
        print('segitiga sembarang')
else:
    print('invalid')