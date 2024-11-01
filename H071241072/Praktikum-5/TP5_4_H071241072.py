string = input("Input your string: ")
    
n = len(string)
for length in range (1, n + 1):
    for i in range (n - length + 1):
        print(string[i:i + length])