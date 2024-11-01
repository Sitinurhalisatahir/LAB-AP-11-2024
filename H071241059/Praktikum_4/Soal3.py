def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = (n * 3) + 1
            print(n)
        langkah += 1
    return langkah

def main():
    try:
        n = int(input("Masukan angka: "))
        jumlah_langkah = hitung_langkah(n)
        print(f"Jumlah langkah: {jumlah_langkah}")
    except ValueError:
        print("Input tidak Valid")
main()