import random

def HartaKarun():
    total_jarak = 0
    bahaya_terdeteksi = False
    gachajarak = random.randint(1, 20)
    print("Selamat datang, Pemburu Harta Karun!")
    print("Misi Anda adalah menempuh 50 meter tanpa langkah berbahaya dan menggali harta karun.")
    
    while True:
        try:
            jarak = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if jarak <= 0:
                break
        
            if jarak > 20 or jarak == gachajarak:
                bahaya_terdeteksi = True
                print("Bruh anda menginjak jalan yang berbahaya")
            else:
                total_jarak += jarak
                print(f"Total jarak: {total_jarak} meter")
            
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            
    if bahaya_terdeteksi:
        print("Ada bahaya : Ya")
        print("Keputusan : Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Ada bahaya : Tidak")
        print("Keputusan : Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan : Tidak menemukan harta karun. Coba lagi!")

HartaKarun()
