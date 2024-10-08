
N = int(input("masukkan angka N: "))  
M = int(input("masukkan angka M: "))   
i = 0
while i < N:
    j = 0 if i % 2 == 0 else M - 1
        # Baris ganjil, bergerak ke kanan
    angka = 1 if i % 2 == 0 else  - 1
        # Baris genap, bergerak ke kiri

    while (j >= 0 and j < M):
        print(f"MOVE ({i}, {j})")
        j += angka
    i+=1
           