n = int(input('input N: '))
m = int(input('input M: '))

for x in range (n):
    if x % 2 == 0:
        for y in range(m):
            print(f'move to ({x},{y})')
    else:
        for y in range(m-1,-1,-1):
            print(f'move to ({x},{y})')