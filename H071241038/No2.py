def kalimat_akronim(kalimat):
    kata_akronim = kalimat.split()

    akronim = ''.join([kata[0].upper() for kata in kata_akronim])
    return akronim

kalimat = input("masukkan kalimat: ")
akronim = kalimat_akronim(kalimat)
print(f"acronym {akronim}")