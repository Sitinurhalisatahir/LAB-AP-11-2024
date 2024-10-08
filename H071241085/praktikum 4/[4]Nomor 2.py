import random

def persentase_jebakan() :
    jebakan0 = random.randint(1,10)
    jebakan1 = random.randint(11,20)
    return jebakan0, jebakan1
print(f'persentase jebakan adalah: {persentase_jebakan()}')

def harta_karun():
    total_jarak = 0
    deteksi_bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan angka (meter) atau tekan 0 untuk selesai: "))
            if  langkah == 0:
                print("Perjalanan dihentikan")
                break
            if langkah < 0:
                print("Masukkan bilangan bulat (bilangan positif)")
                break
            if langkah == persentase_jebakan:
                deteksi_bahaya = True
            else:
                if langkah :
                    deteksi_bahaya = True
            total_jarak += langkah

        except ValueError:
            print("Input tidak valid")


    if total_jarak > 0:
        print(f"Total jarak: {total_jarak}")

        if deteksi_bahaya == True:
            print(f"Bahaya: Ada")
        else:
            print("Bahaya: Tidak ada")

        if total_jarak > 0 and deteksi_bahaya == False:
            print("Aman. Kamu tepat menemukan harta karun dan menang!")
        elif total_jarak > 0 and deteksi_bahaya == True:
            print("Tidak aman untuk menggali harta karun. Coba lagi!")
        else:
            print("Tidak menemukan harta karun. Coba lagi!")


harta_karun()