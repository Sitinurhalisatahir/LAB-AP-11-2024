def akronim(kalimat):
    kata_kata = kalimat.split()
    huruf_pertama = []
    
    for kata in kata_kata:
        if kata: 
            huruf_pertama.append(kata[0].upper())
    
    return ''.join(huruf_pertama)

kalimat_input = input("Masukkan kalimat yang ingin diubah menjadi akronim: ")
hasil_akronim = akronim(kalimat_input)
print(hasil_akronim)


