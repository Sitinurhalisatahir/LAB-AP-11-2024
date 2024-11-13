# Menerima input dari pengguna
karakter = input("Masukkan karakter: ")
kalimat = input("Masukkan kalimat: ")

# Gunakan operator in dan not in untuk memeriksa keberadaan karakter
print(karakter, {True: "ditemukan", False: "tidak ditemukan"}[karakter in kalimat], "dalam " ,kalimat)

