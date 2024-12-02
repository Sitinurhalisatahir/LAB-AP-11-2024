def acronym(frasa):
    kata_kata = frasa.split()
    print(kata_kata)
    akronim = ''.join(kata[0].upper() for kata in kata_kata)
    return akronim

input_frasa = input("Masukkan Frasa/kata: ")
hasil = acronym(input_frasa)
print(hasil)
