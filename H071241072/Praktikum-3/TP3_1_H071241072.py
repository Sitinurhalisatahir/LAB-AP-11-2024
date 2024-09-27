n = int(input("Masukkan Jumlah Baris : "))

if n%2 == 0 :
    for i in range(1, n//2 + 1): #4<=2, 3, 4
        print("  " * (n//2 - i), end="")
        print("* " * (2*i - 1)) #

    for i in range(n//2, 0, -1): #3, 2, 1
        print("  " * (n//2 - i), end="")
        print("* " * (2*i - 1))
else :
    for i in range(1, n//2 + 2): #1, 2, 3, 4,
        print("  " * ((n//2 + 1) - i), end="")
        print("* " * (2*i - 1))

    for i in range(n//2, 0, -1): #4, 3 2 1
        print("  " * ((n//2 + 1) - i), end="")
        print("* " * (2*i - 1))