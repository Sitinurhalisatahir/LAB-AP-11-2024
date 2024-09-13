penggunaan_data = int(input("Masukkan penggunaan data (GB): "))
waktu_penggunaan = input("Masukkan waktu penggunaan (Luar Jam Sibuk/Jam Sibuk): ")
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ")

# Determine package based on criteria
if penggunaan_data < 10:
    if waktu_penggunaan == "luar jam sibuk" and jenis_pengguna == "personal":
        print("Paket A") 
    else:
        print("Tidak ada paket yang cocok")
elif penggunaan_data <= 50:
    if waktu_penggunaan == "jam sibuk" and jenis_pengguna == "personal":
        print("Paket B")
    else:
        print("Tidak ada paket yang cocok")
else: 
    if waktu_penggunaan == "jam sibuk" and (jenis_pengguna == "personal" or jenis_pengguna == "bisnis"):
        print("Paket C")
    elif waktu_penggunaan == "luar jam sibuk" and jenis_pengguna == "bisnis":
        print("Paket D")
    else:
        print("Tidak ada paket yang cocok")