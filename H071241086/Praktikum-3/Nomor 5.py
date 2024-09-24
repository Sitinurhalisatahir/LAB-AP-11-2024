populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari (N): "))

for hari in range(1, N+1):
    if hari % 2 == 1:
        populasi_A = int(populasi_A + populasi_A  * 0.30)
        populasi_B = int(populasi_B + populasi_B  * 0.50)
    else:
        populasi_A = int(populasi_A - populasi_A  * 0.20)
        populasi_B = int(populasi_B - populasi_B  * 0.40)
    print(f"Hari {hari}: populasi A = {populasi_A}, populasi B = {populasi_B}")
    if hari % 5 == 0:
        populasi_A = int(populasi_A * 0.9)
        populasi_B = int(populasi_B * 0.9)
    print(f"hari 5:predator memakan 10% populasi")
       

