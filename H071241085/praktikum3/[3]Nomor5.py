A = int(input('masukkan populasi awal serangga A : '))
B = int(input('masukkan populasi awal serangga B : '))
jumlah_hari = int(input('masukkan jumlah hari : '))

for hari in range(1,jumlah_hari+1):
    if hari % 2 == 1:
        A = A * 1.30
        B = B * 1.50
    else:
        A = A * 0.80
        B = B * 0.60
    # print(f'Hari {hari}: Serangga A = {int(A)}, serangga B ={int(B)}')

    if hari % 5 == 0:
        A = A * 0.90
        B = B * 0.90
        print(f'hari {hari}: predator memakan 10% populasi.')
    print(f'hari {hari}: serangga A = {int(A)}, serangga B {int(B)}')