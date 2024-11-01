def hitung_penghapusan_anagram(s1, s2):
    
    freq1 = {}  # Frekuensi karakter dalam s1
    freq2 = {}  # Frekuensi karakter dalam s2
    
    # Menghitung frekuensi masing-masing karakter dalam s1
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1  # Jika karakter belum ada, inisialisasi dengan 0 lalu tambahkan 1
    
    # Menghitung frekuensi masing-masing karakter dalam s2
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1  # Jika karakter belum ada, inisialisasi dengan 0 lalu tambahkan 1
    
    penghapus = 0  # Inisialisasi total penghapusan
    

    for char in set(s1 + s2):
        penghapus += abs(freq1.get(char, 0) - freq2.get(char, 0))  # Hitung selisih absolut frekuensi karakter
    
    return penghapus 


s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

hasil = hitung_penghapusan_anagram(s1, s2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")


