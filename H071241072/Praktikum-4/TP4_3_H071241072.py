def hitung_langkah():
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            raise ValueError
        
        langkah = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            langkah += 1
            print(n)
        
        print(f"Jumlah langkah: {langkah}")
    
    except ValueError:
        print("Input tidak valid")

hitung_langkah()