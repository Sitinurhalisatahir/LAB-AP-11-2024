sahamToday = 105.0
sahamYesterday = float(input("Masukkan harga saham kemarin : "))

perubahanPersentase = ((sahamToday - sahamYesterday) / sahamToday) * 100

Beli = (perubahanPersentase > 5) * 1
Tahan = (perubahanPersentase < 5 and perubahanPersentase > -3) * 1
Jual = (perubahanPersentase < -3) * 1

rekom1 = Beli * 'Beli' + Tahan * 'Tahan' + Jual * 'Jual'

print(f'Perubahan presentase : {perubahanPersentase:.2f}%')
print(f"Rekomendasi investasi: ",rekom1)
