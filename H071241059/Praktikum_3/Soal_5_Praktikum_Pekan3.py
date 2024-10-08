serangga_A = int(input('Masukkan populasi awal Serangga A: '))
serangga_B = int(input('Masukkan populasi awal Serangga B: '))

hari = int(input('Masukkan jumlah hari: '))

for i in range(1, hari + 1, 1):
    if i % 2 == 1:
        serangga_A = (serangga_A * 130) // 100
        serangga_B = (serangga_B * 150) // 100
        if i != 5:
            print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B = {serangga_B:.0f}')
    else:
        serangga_A = (serangga_A * 80) // 100
        serangga_B = (serangga_B * 60) // 100
        print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B = {serangga_B:.0f}')
        
    if i % 5 == 0:
        serangga_A = (serangga_A * 90) // 100
        serangga_B = (serangga_B * 90) // 100
        print(f'Hari {i}: Predator memakan 10% populasi')
        print(f'Hari {i}: Serangga A = {serangga_A:.0f}, Serangga B: {serangga_B:.0f}')
