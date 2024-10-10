def cetak_substring():
    string = input("Input sebuah string: ")
    n = len(string)
    for panjang in range(1, n+1):
        for i in range(n - panjang + 1):
            print(string[i:i+panjang])

cetak_substring()