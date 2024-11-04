import re

str = input("Masukkan string 45 karakter: ")

pola = r'^[A-Za-z02468]{40}[13579\s]{5}$'
cocok = re.match(pola, str)

if cocok:
    print(True)
else:
    print(False)