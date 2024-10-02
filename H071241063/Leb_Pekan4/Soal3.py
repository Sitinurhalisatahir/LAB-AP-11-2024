def hitung_langkah(n):
    if isinstance(n, int) and n > 0:
        langkah = 0
        while n != 1:
            n = n // 2 if n % 2 == 0 else n * 3 + 1
            print(float(n))
            langkah += 1
        print(f"jumlah langkah: {langkah}")
    else:
        print("input tidak valid")
    
try:
    hitung_langkah(int(input("masukkan angka: ")))
except ValueError:
    print("input tidak valid")