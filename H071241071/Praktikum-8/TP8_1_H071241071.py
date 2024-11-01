import re

pattern = r'^(?=.{45}$)[A-Za-z02468]{40}[13579\s]{5}$'
while True :
    string = input("Masukkan string : ")
    hasil = re.match(pattern, string)
    if hasil :
        print(True)
        break
    else :
        print(False)