teks = input("Masukkan teks yang akan dienkripsi: ")
geser = int(input("Masukkan jumlah pergeseran: "))

def geserhuruf(teks, geser):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    geser = geser % 26
    angka = "0123456789"
    geserangka = geser % 10

    hasil = ""  

    for i in teks:
        if i.lower() in alfabet:  
            posisi = alfabet.index(i.lower())
            posisi_baru = (posisi + geser) % 26  
            if i.isupper():
                hasil += alfabet[posisi_baru].upper()
            else:
                hasil += alfabet[posisi_baru]
        elif i in angka: 
            posisi = angka.index(i)
            posisi_baru = (posisi + geserangka) % 10
            hasil += angka[posisi_baru]
        else:
            hasil += i 

    print(hasil)


geserhuruf(teks, geser)