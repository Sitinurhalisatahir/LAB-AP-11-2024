import random

def kartu():
    kartu_acak = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(kartu_acak)

def hitung_nilai(kartupemain):
    kartu_total = sum(kartupemain)
    if kartu_total > 21 and 11 in kartupemain:
        while kartu_total > 21 and 11 in kartupemain:
            kartupemain[kartupemain.index(11)] = 1
            kartu_total = sum(kartupemain)
    return kartu_total

def main():
    kartupemain = [kartu()]
    kartupemain_total = hitung_nilai(kartupemain) 
    print(f'Kartu anda sekarang adalah: {kartupemain}, total: {kartupemain_total}')
    
    while kartupemain_total <= 21:
        ambil = input('Apakah masih akan mengambil kartu? (y/n)' )
        if ambil == 'y':
            kartupemain.append(kartu())
            kartupemain_total = hitung_nilai(kartupemain)
            print(f'Kartu anda sekarang adalah: {kartupemain}, total: {kartupemain_total}')
            if kartupemain_total >= 21:
                break
        elif ambil == 'n':
            break
    
    kartubandar = [kartu()]
    kartubandar_total = sum(kartubandar)
    print(f'Kartu bandar sekarang adalah: {kartubandar}, total: {kartubandar_total}')

    while kartubandar_total < 17:
        kartubandar.append(kartu())
        kartubandar_total = hitung_nilai(kartubandar)
        print(f'Kartu bandar sekarang adalah: {kartubandar}, total: {kartubandar_total}')
        if kartubandar_total >= 17:
            break
    
    print(f'Total kartu anda: {kartupemain_total}')
    print(f'Total kartu bandar: {kartubandar_total}')
    
    if kartupemain_total > 21:
        print('Anda kalah')
    elif kartubandar_total > 21:
        print('Anda menang')
    elif kartupemain_total == kartubandar_total:
        print('Seri')
    elif kartupemain_total > kartubandar_total:
        print('Anda menang')
    else:
        print('Anda kalah')

main()