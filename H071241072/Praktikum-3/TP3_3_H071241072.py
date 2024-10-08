N = int(input("Masukkan N: ")) #baris 3
M = int(input("Masukkan M: ")) #kolom 4

x, y = 0, 0 #x=baris y=kolom
arah = 1

for i in range(N):#0 1 2
    for j in range(M):#1 2 3
        print(f"MOVE to ({x},{y})")
        y += arah
    y -= arah
    x += 1
    arah *= -1