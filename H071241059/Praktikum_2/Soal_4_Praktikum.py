kouta = int(input('Masukkan jumlah paket data yang digunakan (GB): '))
waktu = input('Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ')
pengguna = input('Apakah anda pengguna Personal atau Bisnis? ')


if kouta < 10 and waktu == 'off-peak' and pengguna == 'personal':
    paket = 'Paket A'
    print(f'Paket yang sesuai: {paket}')
elif 10 <= kouta <= 50 and waktu == 'peak' and pengguna == 'personal':
    paket = 'Paket B'
    print(f'Paket yang sesuai: {paket}')
elif kouta > 50 :
    if waktu == 'peak' and (pengguna == 'personal' or pengguna == 'bisnis') :
        paket = 'Paket C'
        print(f'Paket yang sesuai: {paket}')
    elif waktu == 'off-peak' and pengguna == 'bisnis':
        paket = 'Paket D'
        print(f'Paket yang sesuai: {paket}')
    else:
        print('Tidak ada paket yang cocok')    
else:
    print('Tidak ada paket yang cocok')