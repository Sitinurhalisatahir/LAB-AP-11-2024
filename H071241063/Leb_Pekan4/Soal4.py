def kalkulator(angka_pertama, angka_kedua, operasi):

    if operasi == "+":
         hasil = angka_pertama + angka_kedua
    elif operasi == "-":
         hasil = angka_pertama - angka_kedua
    elif operasi == "*":
         hasil = angka_pertama * angka_kedua
    elif operasi == "/" and angka_kedua != 0:
         hasil = angka_pertama / angka_kedua
    else: 
          hasil = "operasi tidak valid atau pembagian dengan nol!"
    return hasil

angka_pertama = float(input("Angka Pertama : "))
angka_kedua = float(input("Angka Kedua : "))
operasi = input("Operasi (+,-,*,/): ")

hasil = kalkulator(angka_pertama, angka_kedua, operasi)

print("Hasil:",hasil)