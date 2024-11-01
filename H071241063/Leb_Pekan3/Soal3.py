# N = int(input("Masukkan nilai N: "))
# M = int(input("Masukkan nilai M: "))

# for i in range(N):
#     if i % 2 == 0:
#         for j in range(M):
#             print(f"MOVE to ({i},{j})")
#     elif i % 2 == 0:
#             print(f"MOVE to ({i},{j})")
#     else:
#         for j in range(M-1, -1, -1):
#             print(f"MOVE to ({i},{j})")

N = int(input("Masukkan nilai N: "))
M = int(input("Masukkan nilai M: "))

# Variabel baru untuk menyimpan hasil zig-zag tridi
zigzagtridi = []

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            zigzagtridi.append(f"MOVE to ({i},{j})")
    else:
        for j in range(M-1, -1, -1):
            zigzagtridi.append(f"MOVE to ({i},{j})")

# Tampilkan hasil zigzagtridi
for move in zigzagtridi:
    print(move)

