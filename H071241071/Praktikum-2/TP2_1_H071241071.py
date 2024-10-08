Sisi1 = int(input("Masukkan panjang sisi pertama : "))
Sisi2 = int(input("Masukkan panjang sisi kedua : "))
Sisi3 = int(input("Masukkan panjang sisi ketiga : "))

if Sisi1 < 0 or Sisi2 < 0 or Sisi3 < 0 :
    print("Tidak dapat membentuk segitiga yang valid")
elif Sisi1 == Sisi2 == Sisi3 :
    print("Segitiga Sama Sisi")
elif Sisi1 == Sisi2 or Sisi2 == Sisi3 or Sisi1 == Sisi3 :
    print("Segitigas Sama Kaki")
else :
    print("Segitiga Sembarang")
