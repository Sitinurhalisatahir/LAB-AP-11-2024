print("selamat datang dikalkulator sederhana!")

def kalkulator(angka_pertama, angka_kedua,operasi, operasi2 ): 
    n = 0
    while n!=2:
        if operasi == '+':
            hasil = angka_pertama + angka_kedua 
        elif operasi == '-':
            hasil = angka_pertama - angka_kedua
        elif operasi == '*':
            hasil = angka_pertama * angka_kedua 
        elif operasi == '/' and angka_kedua != 0:
            hasil = angka_pertama / angka_kedua 
        else:
            hasil = "operasi tdk valid atau pembagian dgn nol"
        
        angka_pertama = hasil
        angka_kedua = angka_ketiga
        operasi = operasi2
        n+=1
        
    return hasil

angka_pertama = int(input("Masukkan angka pertama: "))
angka_kedua = int(input("Masukkan angka kedua: "))
angka_ketiga = int(input("Masukkan angka ketiga: "))
operasi = input("Masukkan operasi (+, -, *, /): ")
operasi2 = input("Masukkan operasi (+, -, *, /): ")

hasil = kalkulator(angka_pertama, angka_kedua, operasi, operasi2)
print("HASIL : ", hasil)