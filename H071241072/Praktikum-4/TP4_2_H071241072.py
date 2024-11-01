import random

def pemburu_harta():
    total_jarak = 0
    bahaya_terdeteksi = False
    jebakan = random.randint(1, 20)

    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat positif.")
                continue
            elif langkah == 0:
                break
            elif total_jarak > 20 or langkah==jebakan:
                bahaya_terdeteksi = True
                print("Ada bahaya terdeteksi!")

            total_jarak += langkah

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")

    if total_jarak == 50:
        print(f"Total jarak: {total_jarak} meter")
        print("Ada bahaya: Tidak")
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif total_jarak > 50:
        print(f"Total jarak: {total_jarak} meter")
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif bahaya_terdeteksi:
        print("Ada bahaya: Ya")
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print(f"Total jarak: {total_jarak} meter")
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")

pemburu_harta()