str1 = input("Masukkan String Pertama: ") 
str2 = input("Masukkan String Kedua: ")

Hapus = 0
for i in str1:
    if i in str2:
        str2 = str2.replace(i, "", 1)
    else:
        Hapus += 1
        
Hapus += len(str2)
print("Jumlah minimum penghapusan untuk membuat anagram : ", Hapus)