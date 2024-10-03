baris = int(input('masukkan jumlah baris : '))

for ketupat in range(baris):
    if ketupat % 2 == 0:
        print (' '*(baris-ketupat-1)+'* '*(ketupat+1))

for ketupat in range(baris//2+1,-1,-1):
   if ketupat % 2 == 0:
        print(' '*(baris-ketupat-1)+'* '*(ketupat+1))