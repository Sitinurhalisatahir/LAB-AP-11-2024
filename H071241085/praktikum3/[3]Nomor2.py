import random

angka_rahasia = random.randint(1,100)
coba = 0
max_coba  = 5

print('''Tebak angka dari 1 sampai 100! \nMax 5 percobaan!''')

while coba < max_coba:
    tebak = int(input('masukkan tebakan anda (0 utk stop) : '))
    if tebak == 0:
        print('End')
        break
    coba += 1

    if tebak > angka_rahasia:
        print('Angka terlalu besar!')
    elif tebak < angka_rahasia:
        print('Angka terlalu kecil!')
    else:
        print('selamat! tebakan benar!')
        break

    if coba == max_coba:
        print('maaf, anda telah melewati batas percobaan')
        print(f'jawaban yg benar adalah : {angka_rahasia}')