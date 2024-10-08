def kalkulator_sederhana():
    print("Selamat datang di Kalkulator Sederhana!")

    angka1_input = input("Angka pertama: ")
    try:
        angka1 = float(angka1_input)
    except ValueError:
        print(f"Input tidak valid: could not convert string to float: '{angka1_input}'")
        return

    angka2_input = input("Angka kedua: ")
    try:
        angka2 = float(angka2_input)
    except ValueError:
        print(f"Input tidak valid: could not convert string to float: '{angka2_input}'")
        return

    operasi = input("Operasi (+, -, *, /): ")

    if operasi == "+":
        print(f"Hasil: {angka1 + angka2}")
    elif operasi == "-":
        print(f"Hasil: {angka1 - angka2}")
    elif operasi == "*":
        print(f"Hasil: {angka1 * angka2}")
    elif operasi == "/":
        if angka2 != 0:
            print(f"Hasil: {angka1 / angka2}")
        else:
            print("Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Operasi tidak valid. Gunakan +, -, *, atau /.")

kalkulator_sederhana()