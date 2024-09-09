karakter = input("Masukkan Karakter: ")
kalimat = input("Masukkan Kalimat: ")

# Menggunakan operator 'in' untuk memeriksa keberadaan karakter dalam kalimat
output = karakter in kalimat

# Menggunakan operasi indeks untuk memilih bagian kalimat
pesan = ["tidak ditemukan dalam", "merupakan bagian dari"][output]

# Format output sesuai ketentuan
hasil = f"{karakter} {pesan} '{kalimat}'"
print(hasil)