def akronim(kalimat):
    kata_kata = kalimat.split()
    kata_akronim = ''
    
    for kata in kata_kata:
        kata_akronim = kata_akronim + kata[0].upper()
    
    return kata_akronim

kalimat = "Tentara Negara Indonesia"
print(akronim(kalimat))