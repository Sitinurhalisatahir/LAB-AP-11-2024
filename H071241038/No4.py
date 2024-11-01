str = input("Masukkan sebuah string: ")
len = len(str)

for i in range(1, len+1):
    print("A")
    for j in range(len - i + 1):
        print(str[j:j+i])

