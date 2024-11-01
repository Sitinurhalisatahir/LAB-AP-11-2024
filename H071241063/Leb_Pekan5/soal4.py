def print_all_substrings(s):  
    n = len(s)  # Mendapatkan panjang string 's'

    for panjang in range(1, n + 1):  # Loop melalui semua panjang substring (dari 1 hingga n)
        for start in range(n - panjang + 1):  # Loop melalui indeks awal substring
            print(s[start:start + panjang])  # Cetak substring dari 'start' hingga 'start + panjang'

input_string = input("Input your string : ")  
print_all_substrings(input_string)  

