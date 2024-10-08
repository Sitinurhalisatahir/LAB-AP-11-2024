a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

if a + b <= c or a + c <= b or b + c <= a:
  print("Tidak dapat membentuk segitiga yang valid")
else:
  if a == b == c:
    print("Segitiga Sama Sisi")
  elif a == b or a == c or b == c:
    print("Segitiga Sama Kaki")
  else:
    print("Segitiga Sembarang")