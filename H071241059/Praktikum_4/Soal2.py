def cariharta():
    total_langkah = 0
    bahaya = False

    while True:
        try:
            langkah_pemain = int(input('Masukkan langkah (meter) atau 0 untuk selesai: '))
            total_langkah += langkah_pemain
            if langkah_pemain == 0:
                break
            elif langkah_pemain > 20:
                bahaya = True
        except ValueError:
            print('Input tidak valid. Masukkan bilangan bulat.')
    
    print(f'Total jarak: {total_langkah}')

    if bahaya:
        print('Ada bahaya: ya')
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_langkah == 50:
        print('Ada bahaya: Tidak')
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")

cariharta()