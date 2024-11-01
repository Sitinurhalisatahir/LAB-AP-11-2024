penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak): ")
jenis_pengguna = input("Apakah Anda pengguna personal atau bisnis? ")

if penggunaan_data < 10:
    if waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
        paket = "Paket A"
    else:
        paket = "n/a"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == "peak" and jenis_pengguna == "personal":
        paket = "Paket B"
    else:
        paket = "n/a"
else:
    if jenis_pengguna == "personal":
        if waktu_penggunaan == "peak":
            paket = "Paket C"
        else:
            paket = "Paket D"
    elif jenis_pengguna == "bisnis":
        if waktu_penggunaan == "off-peak":
            paket = "Paket D"
        else:
            paket = "Paket C"

if paket == "n/a":
    print("Tidak ada paket yang cocok")
else:
    print("Paket yang sesuai:", paket)