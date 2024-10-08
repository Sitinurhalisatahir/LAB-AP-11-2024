TotalHarga = int(input("Masukkan total harga yang harus dibayarkan: "))
Uang = int(input("Masukkan jumlah uang yang diberikan oleh pelanggan: "))
kembalian = Uang - TotalHarga
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if Uang < TotalHarga :
    print(f"Uang yang anda berikan kurang {abs(kembalian)}")
else :
    for i in pecahan:
        JumlahPecahan = kembalian // i
        if JumlahPecahan > 0:
            print(f"{JumlahPecahan} lembar {i} rupiah")
        kembalian %= i