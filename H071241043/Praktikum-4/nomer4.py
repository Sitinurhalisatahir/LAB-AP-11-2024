# Definisikan fungsi kalkulator
def kalkulator():
    print("SELAMAT DATANG DI KALKULATOR SEDERHANA!!!!!! :D")

    try:
       bilangan1 = float(input("Masukkan bilangan : "))
       bilangan2 = float(input("Masukkan bilangan : "))

    except ValueError as e:
        print(f"Input tidak valid: could not convert string to float: {e}")

    operasi = input("Pilih operasi! (+, -, *, /) : ") 

    if operasi == "+":
           hasil = bilangan1 + bilangan2
           print(f"{bilangan1} + {bilangan2} = {hasil}")

    elif operasi == "-":
           hasil = bilangan1 - bilangan2
           print(f"{bilangan1} - {bilangan2} = {hasil}")
        
    elif operasi == "*":
           hasil = bilangan1 * bilangan2
           print(f"{bilangan1} * {bilangan2} = {hasil}")

    elif operasi == "/":
           if bilangan2 == 0:
              print("PEMBAGIAN DENGAN 0 TIDAK DIPERBOLEHKAN!")
           else:
              hasil = bilangan1 / bilangan2
              print(f"{bilangan1} / {bilangan2} = {hasil}")

    else:
          print("Operasi tidak valid! Gunakan operasi yang telah disediakan!")     

kalkulator()
