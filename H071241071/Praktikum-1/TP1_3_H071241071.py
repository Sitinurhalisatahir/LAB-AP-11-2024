def konversi_detik_ke_waktu(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return f"{jam:02}:{menit:02}:{detik:02}"
Total_Detik = int(input("Masukkan jumlah detik : "))
waktu = konversi_detik_ke_waktu(Total_Detik)
print(waktu)