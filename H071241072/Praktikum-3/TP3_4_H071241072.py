total = int(input("Masukkan total harga: "))
bayar = int(input("Masukkan uang yang diberikan: "))
kembali = bayar - total
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if bayar < total:
    print("Uang anda tidak cukup.")
else:
    for rp in pecahan:
        p = kembali // rp
        if p > 0:
            print(f"{p} lembar Rp{rp}")
        kembali %= rp