populasi_a = int(input("Masukkan populasi awal Serangga A: "))
populasi_b = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, jumlah_hari + 1):
    if hari %2 != 0:
        populasi_a = populasi_a * 130 // 100
        populasi_b = populasi_b * 150 // 100
    else:
        populasi_a = populasi_a * 80 // 100
        populasi_b = populasi_b * 60 // 100
    if hari %5 ==0:
        populasi_a = populasi_a * 90// 100
        populasi_b = populasi_b * 90 // 100
        print(f"Hari {hari}: Predator memakan 10% populasi.")
    
    print(f"Hari {hari}: Serangga A = {populasi_a}, Serangga B = {populasi_b}")