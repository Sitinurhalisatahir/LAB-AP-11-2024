total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

if uang_diberikan < total_harga:
    print("Uang yang diberikan kurang!")
else:
    kembalian = uang_diberikan - total_harga
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    
    print("Kembalian:")
    for nilai in pecahan:
        if kembalian >= nilai:
            jumlah = kembalian // nilai
            print(f"{jumlah} lembar Rp {nilai:,}")
            kembalian = kembalian % nilai