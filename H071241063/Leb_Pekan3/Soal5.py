def prediksi_populasi(a, b, hari):
    n = 1
    while n <= hari:
        if n % 2 == 1:
            a = int(a * 1.3)
            b = int(b * 1.5)
        else:
            a = int(a * 0.8)
            b = int(b * 0.6)
        
        print(f"Hari {n}: Serangga A = {a}, Serangga B = {b}")
        
        if n % 5 == 0:
            print(f"Hari {n}: Predator memakan 10% populasi.")
            a = int(a * 0.9)
            b = int(b * 0.9)
            print(f"Hari {n}: Serangga A = {a}, Serangga B = {b}")
        
        n += 1

a = int(input("Masukkan populasi awal Serangga A: "))
b = int(input("Masukkan populasi awal Serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

prediksi_populasi(a, b, hari)