def caesar_cipher_encrypt(text,shift):
    hasil = []

    for i in text:
        if i.isalpha():  
            batas = ord('A') if i.isupper() else ord('a')
            hasil.append(chr((ord(i) - batas + shift) % 26 + batas))
        else:
            hasil.append(i)

    return ''.join(hasil)

text = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))
enkripsi_output = caesar_cipher_encrypt(text, shift)

print(ord("A"))
print(chr(1))
print("Text : ", text)
print("shift :", shift)
print("Hasil enkripsi:", enkripsi_output)

#ascii A = 65, ascii a = 97