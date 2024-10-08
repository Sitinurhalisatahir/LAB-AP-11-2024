populasi_A = int(input("masukkan populasi awal serangga A :"))
populasi_B = int(input("masukkan populasi awal serangga B :"))
jumlah_hari = int(input("masukkan jumlah hari : "))
i = 0

while i < jumlah_hari:
    i = i + 1
    if jumlah_hari % 2 == 1:
        populasi_A = int(populasi_A + populasi_A * 0.3)
        populasi_B = int(populasi_B + populasi_B * 0.5)
    else:
        populasi_A = int(populasi_A - populasi_A * 0.2)
        populasi_B = int(populasi_B - populasi_B * 0.4)
    
    if jumlah_hari % 5 == 0 :
        populasi_A = int(populasi_A - populasi_A * 0.1)
        populasi_B = int(populasi_B - populasi_B * 0.1)
        print(f"hari {i}: predator memakan 10% populasi.")

    print(f"hari {i}: serangga A =  {populasi_A}, serangga B = {populasi_B} ")