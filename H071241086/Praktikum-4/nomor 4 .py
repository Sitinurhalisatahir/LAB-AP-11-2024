print("selamat datang dikalkulator sederhana!")

def kalkulator(angka_pertama, angka_kedua, operasi):
    if operasi == '+':
        return angka_pertama + angka_kedua
    elif operasi == '-':
        return angka_pertama - angka_kedua
    elif operasi == '*':
        return angka_pertama * angka_kedua
    elif operasi == '/':
        if angka_kedua == 0:
            return "Pembagian dengan nol tidak diperbolehkan."
        else:
            return angka_pertama / angka_kedua
    else:
        return "Operasi tidak valid. Gunakan +, -, *, atau /."

angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")

# Memanggil fungsi dan menampilkan hasil
hasil = kalkulator(angka_pertama, angka_kedua, operasi)
print(f"Hasil: {hasil}")