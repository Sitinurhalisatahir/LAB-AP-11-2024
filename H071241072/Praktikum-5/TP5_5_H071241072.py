text = input("Masukkan String: ")
shift = int(input("Masukkan jumlah pergeseran: "))
chiper = ""
    
for huruf in text:
    if huruf.isupper():
        chiper += chr((ord(huruf) + shift - 65) % 26 + 65)
    elif huruf.islower():
        chiper += chr((ord(huruf) + shift - 97) % 26 + 97)
    else:
        chiper += huruf

print(f'Text  : {text}')
print(f'Shift : {shift}')
print(f'Chiper: {chiper}')