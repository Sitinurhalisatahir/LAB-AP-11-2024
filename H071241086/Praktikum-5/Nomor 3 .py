import string

def min_deletions_to_make_anagram(s1, s2):
    # Menghapus karakter spesial agar s1 dan s2 setara
    s1 = ''.join(filter(lambda c: c in string.ascii_letters, s1)).lower() 
    s2 = ''.join(filter(lambda c: c in string.ascii_letters, s2)).lower()
    
    # Menghitung frekuensi karakter dalam kedua string
    freq1 = {} 
    freq2 = {}

    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

# Menghitung jumlah penghapusan yang diperlukan
    deletions = 0

    # Menghitung karakter yang ada di freq1
    for char in freq1:
        if char in freq2:
            deletions += abs(freq1[char] - freq2[char])
        else:
            deletions += freq1[char]

    # Menghitung karakter yang hanya ada di freq2
    for char in freq2:
        if char not in freq1:
            deletions += freq2[char]

    return deletions

# Mengambil input dari pengguna
s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")
result = min_deletions_to_make_anagram(s1, s2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {result}")