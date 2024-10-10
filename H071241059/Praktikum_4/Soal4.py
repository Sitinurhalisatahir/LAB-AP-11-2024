print('Selamat datang di kalkulator sederhana!')

def calculator():
    try:
        angka1 = float(input('Angka 1 : '))
        angka2 = float(input('Angka 2 : '))
        alat = input('Operasi (+, -, *, /): ')
        if alat == '+':
            hasil = angka1 + angka2
            print(f'Hasil: {hasil}')
        elif alat == '-':
            hasil = angka1 - angka2
            print(f'Hasil: {hasil}')
        elif alat == '*':
            hasil = angka1 * angka2
            print(f'Hasil: {hasil}')
        elif alat == '/':
            if angka2 != 0:  
                hasil = angka1 / angka2
                print(f'Hasil: {hasil}')
            else:
                print('Pembagian dengan nol tidak diperbolehkan.')
        else:
            print('Operasi tidak valid. Gunakan +, -, *, atau /.')
    except ValueError:
        print('Input tidak valid: could not convert string to float: a')
    
calculator()