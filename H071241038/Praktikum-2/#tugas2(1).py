#tugas2

panjang_sisi_pertama = int(input("masukkan panjang sisi pertama: "))
panjang_sisi_kedua = int(input("masukkan panjang sisi kedua: "))
panjang_sisi_ketiga = int(input("masukkan panjang sisi ketiga: "))

if panjang_sisi_pertama == panjang_sisi_kedua == panjang_sisi_ketiga > 0:
    print("segitiga sama sisi")
    if panjang_sisi_pertama <= 0 or panjang_sisi_kedua <= 0 or panjang_sisi_ketiga <= 0 or panjang_sisi_pertama + panjang_sisi_kedua <= panjang_sisi_ketiga or panjang_sisi_kedua + panjang_sisi_ketiga <= panjang_sisi_pertama or panjang_sisi_pertama + panjang_sisi_kedua <= panjang_sisi_ketiga:
        print("segitiga tidak valid")
elif panjang_sisi_pertama == panjang_sisi_kedua > 0 or panjang_sisi_pertama == panjang_sisi_ketiga > 0 or panjang_sisi_kedua == panjang_sisi_ketiga > 0:
    print("segitiga sama kaki")
elif panjang_sisi_pertama > 0 and  panjang_sisi_kedua > 0 and panjang_sisi_ketiga > 0:
    print("segitiga sembarang")
else:
    print("segitiga tidak valid")
