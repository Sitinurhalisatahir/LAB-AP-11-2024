populasi_seranggaA = int(input("masukkan populasi awal serangga A: "))
populasi_seranggaB = int(input("masukkan populasi awal serangga B: "))
Jumlah_hari = int(input("masukkan jumlah hari: "))

for i in range (1, Jumlah_hari + 1):
    if (i%5) == 0: #untuk hari ke 5 dan 10
        populasi_seranggaA = populasi_seranggaA * 90//100
        populasi_seranggaB = populasi_seranggaB * 90//100
        print(f"hari {i} Predator memakan 10% populasi")
    
    if (i%2) == 0:
            populasi_seranggaA = populasi_seranggaA * 80/100
            populasi_seranggaB = populasi_seranggaB * 60/100
            print(f"hari {i}: Serangga A = {round(populasi_seranggaA)} , Serangga B = {round(populasi_seranggaB)}  ")

    elif (i%2) != 0:
            populasi_seranggaA = populasi_seranggaA * 130/100
            populasi_seranggaB = populasi_seranggaB * 150/100
            print(f"hari {i}: Serangga A = {round(populasi_seranggaA)} , Serangga B = {round(populasi_seranggaB)}  ")

