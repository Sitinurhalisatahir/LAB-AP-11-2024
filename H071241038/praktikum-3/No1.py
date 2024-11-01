Jumlah_baris = int(input("masukkan jumlah baris untuk setengah belah ketupat: "))

for i in range(1, Jumlah_baris+1):
    if i % 2 == 1:
        print(" " * (Jumlah_baris - i), end=" ")
        print("*" * (2 * i - 1))

for i in range(Jumlah_baris - 1, 0, -1):
    if i % 2 == 1:
        print(" " * (Jumlah_baris - i), end=" ")
        print("*" * (2 * i - 1))