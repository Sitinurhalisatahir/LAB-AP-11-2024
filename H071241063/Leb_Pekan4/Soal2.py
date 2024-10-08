def pemburu_harta_karun():
    total_jarak = 0
    mendeteksi_bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesei: "))
            if langkah < 0:
                print("input tidak valid. masukkan bilangan bulat.")
                continue
            if langkah == 0:
                break
            if langkah > 20:
                mendeteksi_bahaya = True
            total_jarak += langkah
        except ValueError:
            print("input tidak valid.masukkan bilangan bulat.")   
        
    print(f"total jarak: {total_jarak} meter")
    if total_jarak == 50 and not medeteksi_bahaya:
        print("keputusan : aman!. kamu telah menemukan harta karun dan menang!")
    elif mendeteksi_bahaya:
        print("keputudan: tidak aman untuk menggali harta karun.coba lagi")
    else:
        print("keputusan: tidak menemukan harta karun. coba lagi")

pemburu_harta_karun()


    