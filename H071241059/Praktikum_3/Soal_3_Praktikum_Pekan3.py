N = int(input('N = '))
M = int(input('M = '))
O = int(input('O = '))

for x in range(N):
    if x % 2 == 0:
        for y in range(M):
            if y % 2 == 0:
                for z in range(O):
                    print(f'MOVE to ({x},{y},{z})')
            else:
                for z in range (O - 1, -1, -1):
                    print(f'MOVE to ({x},{y},{z})')
    else:
        for y in range(M - 1, -1, -1):
            if y % 2 == 0:
                for z in range (O - 1, -1, -1):
                    print(f'MOVE to ({x},{y},{z})')
            else:
                for z in range (O):
                    print(f'MOVE to ({x},{y},{z})')
            