#Rekomendasi paket internet

PenggunaanData = int(input("Masukkan jumlah data yang digunakan (GB) : "))
WaktuPengunaan = input("Tentukan waktu penggunaan! (Off-Peak/Peak) : ")
JenisPengguna = input("Untuk penggunaan Personal atau Bisnis : ")

#Pengunaan Data
ringan = PenggunaanData < 10
sedang = PenggunaanData >= 10 and PenggunaanData <= 50
berat = PenggunaanData > 50

#Paket yang ditawarkan
if PenggunaanData > 0 and (WaktuPengunaan == "Off-Peak" or WaktuPengunaan == "Peak") and (JenisPengguna == "Personal" or JenisPengguna == "Bisnis"):
    if ringan and WaktuPengunaan == "Off-Peak" and JenisPengguna == "Personal": 
        print("Paket A")

    elif sedang and WaktuPengunaan == "Peak" and JenisPengguna == "Personal": 
        print("Paket B")

    elif berat and WaktuPengunaan == "Peak" and (JenisPengguna == "Personal" or JenisPengguna == "Bisnis"): 
        print("Paket C")

    elif berat and WaktuPengunaan == "Off-Peak" and JenisPengguna == "Bisnis": 
        print("Paket C")

else:
    print("Tidak ada paket yang cocok")