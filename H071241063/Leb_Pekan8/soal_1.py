import re

string = input("Masukkan sebuah kalimat yang terdiri dari 45 karakter: ")

if len(string) == 45:
    pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    if re.fullmatch(pattern, string):
        print("True")
    else:
        print("False")
else:
    print("False")


