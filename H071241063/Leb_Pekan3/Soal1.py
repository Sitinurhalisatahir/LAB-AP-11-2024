jumlah_bariss = int(input("Masukkan jumlah baris : "))

bilangan =  "*"

if jumlah_bariss <= 0:
    print("masukkan angka yang benar")
  
elif jumlah_bariss % 2 == 0:
    for i in range(jumlah_bariss // 2):
        print(" " * (jumlah_bariss - i - 1) + bilangan * (2 * i + 1))

    for i in range((jumlah_bariss // 2) - 1, -1, -1):
        print(" " * (jumlah_bariss - i - 1) + bilangan * (2 * i + 1))

# elif jumlah_bariss % 2 != 0:
#     for i in range((jumlah_bariss // 2)+ 1):
#         print(" " * (jumlah_bariss - i - 1) + bilangan * (2 * i + 1))

#     for i in range((jumlah_bariss // 2) - 1, -1, -1):
#         print(" " * (jumlah_bariss - i - 1) + bilangan * (2 * i + 1))
        
    
        
        




