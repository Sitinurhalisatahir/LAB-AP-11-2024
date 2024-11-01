def caesar_cipher(text, shift):
    huruf_kecil = 'abcdefghijklmnopqrstuvwxyz'  
    huruf_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
    result = ''  

    for char in text:  # Looping untuk setiap karakter dalam string input
        if char in huruf_kecil:  # Jika karakter adalah huruf kecil
            index = huruf_kecil.index(char)  # Mendapatkan index karakter dalam alfabet huruf kecil
            new_index = (index + shift) % 26  # Menghitung index baru setelah pergeseran
            result += huruf_kecil[new_index]  # Menambahkan huruf baru hasil pergeseran ke result
        
        elif char in huruf_besar:  # Jika karakter adalah huruf besar
            index = huruf_besar.index(char)  # Mendapatkan index karakter dalam alfabet huruf besar
            new_index = (index + shift) % 26  # Menghitung index baru setelah pergeseran
            result += huruf_besar[new_index]  # Menambahkan huruf baru hasil pergeseran ke result
        
        else:
            result += char  # Jika bukan huruf (misal: spasi atau tanda baca), langsung tambahkan ke result
    
    return result  # Mengembalikan hasil enkripsi


text = input("Masukkan String: ")  
shift = int(input("Masukkan jumlah pergeseran: "))  

encrypted_text = caesar_cipher(text, shift)

print(f"Text : {text}")
print(f"Shift : {shift}") 
print(f"Cipher: {encrypted_text}")  
