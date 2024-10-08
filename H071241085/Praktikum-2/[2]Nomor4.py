data_kuota = int(input('Masukkan jumlah data yg dipergunakan (GB) : '))
peak = input('Mayoritas digunakan di luar jam sibu (off-peak) atau di jam sibuk (peak) ? : ')
pengguna = input('Apakah anda pengguna Personal atau Bisnis? : ')

if data_kuota < 10:
    if peak == 'off-peak' and pengguna == 'personal':
        print('Paket A')
    else:
        print('Tidak ada paket yg cocok')
elif 10 <= data_kuota <= 50:
    if peak == 'peak' and pengguna == 'personal':
        print('Paket B')
    else:
        print('Tidak ada paket yg cocok')
elif data_kuota > 50:
    if (pengguna == 'personal' or pengguna == 'bisnis') and peak == 'peak':
    # if peak == 'peak' and pengguna == 'personal' or pengguna == 'bisnis':
        print('Paket C')
        # if peak == 'off-peak' and pengguna == 'bisnis':
        #     print('Paket D')
        # else:
        #     print('Tidak ada paket yg cocok')
    else:
        print('Paket D')
# elif data_kuota >= 50:
#     if peak == 'off-peak' and pengguna == 'bisnis':
#         print('Paket D')
#     else:
#         print('Tidak ada paket yg cocok')
else:
    print('Tidak ada paket yg cocok')