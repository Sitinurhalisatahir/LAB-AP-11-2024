def jika_genap(n):
    return n // 2

def jika_ganjil(n):
    return (n * 3) + 1

def teka_teki():
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        proses = 0
        if n <= 0:
            print("HANYA BILANGAN POSITIF YANG BOLEH DIINPUT!")
        else:

            while n > 1:
                if n % 2 == 0:
                    n = jika_genap(n)
                else:
                    n = jika_ganjil(n)
                print(n)
                proses += 1
            print(f"Jumlah langkah: {proses}")

    except ValueError:
        print("Input tidak valid")

teka_teki()