Kalimat = input("Masukkan kalimat : ")
acronym = ''.join([i[0].upper() for i in Kalimat.split()])
print(acronym)