a = int(input("Masukkan Panjang sisi pertama: "))
b = int(input("Masukkan Panjang sisi kedua: "))
c = int(input("Masukkan Panjang sisi ketiga: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")