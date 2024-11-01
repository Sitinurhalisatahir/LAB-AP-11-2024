A = int(input("Masukkan populasi awal Serangga A: "))
B = int(input("Masukkan populasi awal Serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for i in range(1, hari + 1):
    if i % 2 != 0:
        A = int(A * 1.30)
        B = int(B * 1.50)
    else:
        A = int(A * 0.80)
        B = int(B * 0.60)
    if i % 5 == 0:
        print(f"Hari {i}: Predator memakan 10% populasi.")
        A = int(A * 0.90)
        B = int(B * 0.90)
        
    print(f"Hari {i}: Serangga A = {int(A)} Serangga B = {int(B)}")