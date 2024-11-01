def caesar_cipher(text, shift):
    encrypted_text = []

    for char in text:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            if char.islower():  # Untuk huruf kecil
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:  # Untuk huruf besar
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text.append(new_char)#menambahkan karakter
        else:
            # Karakter lain (angka, spasi, karakter spesial) tetap tidak berubah 
            encrypted_text.append(char)

    return ''.join(encrypted_text)

# Mengambil input dari pengguna
input_string = input("Masukkan String: ")
shift_value = int(input("Masukkan jumlah pergeseran: "))

# Proses enkripsi
ciphered_text = caesar_cipher(input_string, shift_value)

# Output hasil
print(f"Text: {input_string}")
print(f"Shift: {shift_value}")
print(f"Cipher: {ciphered_text}") 