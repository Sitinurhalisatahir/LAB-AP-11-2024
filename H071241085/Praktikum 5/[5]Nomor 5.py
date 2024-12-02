String = input("Masukkan string : ")
pergeseran = int(input("Masukkan jumlah pergeseran : "))

Cipher = ""

for huruf in String:
    if 'a' <= huruf <= 'z':
        hurufbaru = chr((ord(huruf) - ord('a') + pergeseran) % 26 + ord('a'))
        Cipher += hurufbaru
    elif 'A' <= huruf <= 'Z':
        hurufbaru = chr((ord(huruf) - ord('A') + pergeseran) % 26 + ord('A'))
        Cipher += hurufbaru
    elif '0' <= huruf <= '9':
        hurufbaru = chr((ord(huruf) - ord('0') + pergeseran) % 10 + ord('0'))
        Cipher += hurufbaru
    else:
        Cipher += huruf
    print(chr((ord(huruf) - ord('A') + pergeseran) % 26 + ord('A')))
print("Text :", String)
print("Shift :", pergeseran)
print("Cipher :", Cipher)