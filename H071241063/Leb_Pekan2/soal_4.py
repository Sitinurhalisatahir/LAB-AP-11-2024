
data_gb = float(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ")


if data_gb < 10 and waktu_penggunaan == 'off-peak' and jenis_pengguna == 'personal':
    paket = "Paket A"
elif 10 <= data_gb <= 50 and waktu_penggunaan == 'peak' and jenis_pengguna == 'personal':
    paket = "Paket B"
elif data_gb > 50:
    if waktu_penggunaan == 'peak':
        paket = "Paket C" if jenis_pengguna == 'personal' else "Paket D"
    elif waktu_penggunaan == 'off-peak' and jenis_pengguna == 'bisnis':
        paket = "Paket D"
else:
    paket = "Tidak ada paket yang cocok"


print(f"Paket yang sesuai: {paket}")





