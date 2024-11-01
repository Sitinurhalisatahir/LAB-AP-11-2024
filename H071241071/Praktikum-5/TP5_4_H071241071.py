string = input("Input your string: ")

print("="*20)
    
n = len(string)
for i in range (1, n + 1):
    for j in range (n - i + 1):
        print(string[j:j + i])