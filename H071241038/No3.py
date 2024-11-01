str1= input("masukkan string pertama: ")
str2= input("masukkan string kedua: ")
def hitung_frekuensi(str):
    frek = dict()
    for i in str:
        if i in frek:
            frek[i] += 1  
        else:
             frek[i] = 1 
    return frek

frek1 = hitung_frekuensi(str1)
frek2 = hitung_frekuensi(str2)

# key = Value
# a = 10
def total_penghapusan():
    total = 0
    for i in frek1:
        if i in frek2:
            total += abs(frek1[i] - frek2[i])
        else:
            total += frek1[i]
    for i in frek2:
        if i not in frek1:
            total+=frek2[i]
    return total
            
print(frek1)
print(frek2)
print(f"yang harus di hapus : ", total_penghapusan())

# print(frek1["a"])