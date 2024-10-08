#INPUT DARI PENGGUNA
a = float(input("Masukkan panjang sisi pertama : "))
b = float(input("Masukkan panjang sisi kedua : "))
c = float(input("Masukkan panjang sisi ketiga : "))

#KONDISI A,B,C
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or a == c or b == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")
else:
    print("Tidak dapat membentuk segitiga yang valid")


