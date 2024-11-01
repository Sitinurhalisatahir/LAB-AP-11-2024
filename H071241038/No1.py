def cek_palindrom(palindrom):
    if palindrom == palindrom[::-1]:
        return True
    else:
        return False
    
palindrom = input("masukkan palindrom: ").lower()
if cek_palindrom(palindrom):
    print("palindrom")
else:
    print("Not palindrom")