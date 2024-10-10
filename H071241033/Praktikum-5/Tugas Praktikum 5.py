'''SOAL 1'''
def polindrom():
    inputKata = input("Masukkan sebuah kata atau kalimat: ").lower()
    hasilBalik = "".join(reversed(inputKata))
    print(f"Setelah dibalik: {hasilBalik}")
    if inputKata == hasilBalik:
        print("Termasuk palindrome")
    else:
        print("Bukan Palindrom")

'''UNCOMMENT UNTUK JALANKAN PROGRAM'''
# polindrom()

# __________________________________________________________________

'''SOAL 2'''
def acronym():
    kalimat = input("Masukkan sebuah kalimat: ").split()
    list_akronim = []
    for huruf in kalimat:
        list_akronim.append(huruf[0].upper())
    akronim = ''.join(list_akronim)
    print(f"Akronmim: {akronim}")

'''UNCOMMENT UNTUK JALANKAN PROGRAM'''
# acronym()

# _________________________________________________________________

'''SOAL 3'''
def penghapusan_minimum():
    # Buat dictionary untuk menyimpan frekuensi huruf dalam setiap string
    frekuensi_s1 = {}
    frekuensi_s2 = {}

    s1 = input("Masukkan string pertama: ").lower()
    s2 = input("Masukkan string kedua: ").lower()

    # Hitung frekuensi huruf dalam setiap string
    for karakter in s1:
        if karakter.isalpha():  # abaikan simbol
            if karakter in frekuensi_s1:
                frekuensi_s1[karakter] += 1
            else:
                frekuensi_s1[karakter] = 1

    for karakter in s2:
        if karakter.isalpha():  # abaikan simbol
            if karakter in frekuensi_s2:
                frekuensi_s2[karakter] += 1
            else:
                frekuensi_s2[karakter] = 1

    # Hitung jumlah minimum penghapusan karakter yang diperlukan
    penghapusan = 0
    for karakter in frekuensi_s1:
        if karakter in frekuensi_s2:
            penghapusan += abs(frekuensi_s1[karakter] - frekuensi_s2[karakter])
        else:
            penghapusan += frekuensi_s1[karakter]

    for karakter in frekuensi_s2:
        if karakter not in frekuensi_s1:
            penghapusan += frekuensi_s2[karakter]

    print("Jumlah penghapusan minimum:", penghapusan)      

'''UNCOMMMENT UNTUK JALANKAN PROGRAM'''
# penghapusan_minimum()

# _________________________________________________________________

'''SOAL 4'''
def cetak_substring():
    string = input("Input sebuah string: ")
    n = len(string)
    for panjang in range(1, n+1):
        for i in range(n - panjang + 1):
            print(string[i:i+panjang])

'''UNCOMMENT UNTUK JALANKAN PROGRAM'''
# cetak_substring()

# _________________________________________________________________

'''SOAL 5'''
def caesar_cipher():
    kalimat = input("Masukkan string: ")
    shift = int(input("Masukkan jumlah pergeseran: "))

    cipher = ""
    for karakter in kalimat:
        if karakter.isalpha():
            ascii_offset = 65 if karakter.isupper() else 97
            cipher += chr((ord(karakter) - ascii_offset + shift) % 26 + ascii_offset)
        elif karakter.isdigit():
            # ascii_offset = 48
            cipher += str((int(karakter) + shift) % 10)
        else:
            cipher += karakter
    print(f"Text : {kalimat}")
    print(f"Shift : {shift}") 
    print(f"Cipher: {cipher}")
'''UNCOMMENT UNTUK JALANKAN PROGRAM'''
# caesar_cipher()