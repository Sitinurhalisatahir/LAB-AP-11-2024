def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Pembagian dengan 0 tidak diperbolehkan"
    else:
        return a / b

def kalkulator():
    print("Selamat datang di kalkulator sederhana!")

    try:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        operasi = input("Pilih operasi (+, -, *, /): ")
        if operasi == "+":
            print(f"{a} + {b} = {tambah(a,b)}")
        elif operasi == "-":
            print(f"{a} - {b} = {kurang(a,b)}")
        elif operasi == "*":
            print(f"{a} * {b} = {kali(a,b)}")
        elif operasi == "/":
                print(f"{a} / {b} = {bagi(a,b)}")
        else:
            print("Operasi tidak valid. Gunakan +, -, *, atau /")
    except ValueError:
        print("Input tidak valid")

kalkulator()