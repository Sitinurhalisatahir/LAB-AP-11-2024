def palindrome(s):
    # Menghapus spasi dan mengubah ke huruf kecil
    s = s.replace(" ", "").lower()
    
    # Memeriksa apakah string sama dengan kebalikannya
    if s == s[::-1]: #step: -1, yang berarti kita mengambil elemen dari belakang ke depan.
        print("Palindrome")
    else:
        print("Bukan Palindrome")

input_string = input("Masukkan string: ")
palindrome(input_string)

