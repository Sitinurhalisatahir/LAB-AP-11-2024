def cek_bahaya(jarak):
    return jarak > 20

def main():
    total_jarak = 0
    bahaya_terdeteksi = False
    
    print("Selamat datang, Pemburu Harta Karun!")
    print("Anda harus mencapai total jarak 50 meter untuk menemukan harta karun.")
    
    while True:
        try:
            langkah = int(input("Masukkan jarak langkah (meter) atau 0 untuk berhenti: "))
            if langkah == 0:
                break
            elif langkah < 0:
                print("Input tidak valid. Masukkan jarak langkah positif.")
                return
            elif cek_bahaya(langkah):
                bahaya_terdeteksi = True
                print("Langkah terlalu besar! Ada jebakan yang berbahaya!")

            total_jarak += langkah
            print(f"Total jarak: {total_jarak} meter")
            
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang benar.")
            continue
    
    if bahaya_terdeteksi:
        print("Ada bahaya!.")
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Tidak ada bahaya.")
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

# Menjalankan permainan
main()
