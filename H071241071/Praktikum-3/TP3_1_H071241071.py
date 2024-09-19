n = int(input("Masukkan Jumlah Baris : "))

for i in range(1, n//2 + 1):
    print("/" * (n//2 - i))
    print("* " * (2*i - 1))

for i in range(n//2, 0, -1):
    print("  " * (n//2 - i), end="")
    print("* " * (2*i - 1))