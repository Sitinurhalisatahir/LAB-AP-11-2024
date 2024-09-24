pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
total_harga = int(input("Masukkan total harga yang harus dibayarkan: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan: "))

kembalian = uang_diberikan - total_harga
if kembalian < 0:
    print("Uang yang diberikan tidak cukup.")
else:
    print(f"Kembalian: {kembalian}")
    
    for pecahan in pecahan_uang:
        jumlah_lembar = kembalian // pecahan
        if jumlah_lembar > 0:
            print(f"{jumlah_lembar} lembar uang {pecahan}")
        kembalian %= pecahan
