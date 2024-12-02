String1 = input("Masukkan string pertama: ")
String2 = input("Masukkan string kedua: ")
Hapus = 0
for kata in String1:
    if kata in String2:
        String2 = String2.replace(kata,"",1)
    else:
        Hapus+=1
Hapus+=len(String2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {Hapus}")