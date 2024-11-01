Penggunaan_Data = int(input("Masukkan jumlah data yang digunakan (GB): "))
Waktu_Penggunaan = input("Apakah mayoritas penggunaan di Luar Jam Sibuk (Off-Peak) atau Jam Sibuk (Peak)? (off-peak/peak): ")
Tipe_Pengguna = input("Apakah Anda Pengguna Personal atau Bisnis? (personal/bisnis): ")

if Penggunaan_Data < 10 and Waktu_Penggunaan == "off-peak" and Tipe_Pengguna == "personal":
    Paket = "Paket A"
elif 10 <= Penggunaan_Data <= 50 and Waktu_Penggunaan == "peak" and Tipe_Pengguna == "personal":
    Paket = "Paket B"
elif Penggunaan_Data > 50 and Waktu_Penggunaan == "peak" and (Tipe_Pengguna == "personal" or Tipe_Pengguna == "bisnis"):
    Paket = "Paket C"
elif Penggunaan_Data > 50 and Waktu_Penggunaan == "off-peak" and Tipe_Pengguna == "bisnis":
    Paket = "Paket D"
else:
    Paket = "Tidak ada paket yang cocok"

print(f"Paket yang cocok untuk Anda adalah: {Paket}")
