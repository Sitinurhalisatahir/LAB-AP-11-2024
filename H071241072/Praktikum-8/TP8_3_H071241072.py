import re

def validate_username(username):
    '''
    Memvalidasi apakah username sesuai dengan aturan berikut:
    - Panjangnya antara 5 hingga 20 karakter.
    - Harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu angka.
    - Hanya berisi huruf (A-Z, a-z) dan angka (0-9).
    '''
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{5,20}$'
    '''
    Pola regex:
    - `^(?=.*[a-z])`: Memastikan setidaknya ada satu huruf kecil.
    - `(?=.*[A-Z])`: Memastikan setidaknya ada satu huruf besar.
    - `(?=.*\d)`: Memastikan setidaknya ada satu digit.
    - `[A-Za-z\d]{5,20}`: Mengatur panjang karakter antara 5 hingga 20 karakter, hanya terdiri dari huruf dan angka.
    '''
    return re.search(pattern, username)

def validate_email(email):
    '''
    Memvalidasi apakah email sesuai dengan aturan berikut:
    - Hanya terdiri dari huruf kecil dan angka.
    - Format yang diterima: 'username99@example.com' atau 'myuser123@example.co.id'.
    - Domain utama hanya terdiri dari huruf kecil.
    - Domain tingkat atas adalah dua hingga tiga huruf kecil (seperti .com atau .id).
    - Domain tingkat kedua (opsional) harus mengikuti format titik diikuti dua hingga tiga huruf kecil (seperti `.co.id`).
    - Dapat diakhiri dengan dua atau lebih digit angka (opsional).
    '''
    pattern = r'^[a-z]+[a-z0-9]*@[a-z]+\.[a-z]{2,3}(\.[a-z]{2,3})?(\d{2,})?$'
    '''
    Pola regex:
    - `^[a-z]+`: Nama pengguna dimulai dengan satu atau lebih huruf kecil (`a-z`).
    - `[a-z0-9]*`: Mengizinkan huruf kecil atau angka setelah huruf pertama sebagai bagian nama pengguna.
    - `@`: Karakter '@' memisahkan nama pengguna dan domain.
    - `[a-z]+`: Domain utama (seperti `example`) hanya terdiri dari huruf kecil.
    - `\.`: Karakter titik literal sebelum domain tingkat atas.
    - `[a-z]{2,3}`: Domain tingkat atas harus terdiri dari 2 hingga 3 huruf kecil, seperti `com` atau `id`.
    - `(\.[a-z]{2,3})?`: Opsional, untuk domain tingkat kedua seperti `.co.id`.
    - `(\d{2,})?`: Opsional, memungkinkan dua atau lebih angka di akhir.
    '''
    return re.search(pattern, email)

def validate_password(password):
    '''
    Memvalidasi apakah password sesuai dengan aturan berikut:
    - Panjang minimal 8 karakter.
    - Harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu angka.
    - Tidak mengandung simbol atau karakter khusus.
    '''
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    '''
    Pola regex:
    - `(?=.*[a-z])`: Memastikan setidaknya ada satu huruf kecil.
    - `(?=.*[A-Z])`: Memastikan setidaknya ada satu huruf besar.
    - `(?=.*\d)`: Memastikan setidaknya ada satu digit.
    - `[A-Za-z\d]{8,}`: Mengatur panjang minimum 8 karakter, hanya terdiri dari huruf dan angka.
    '''
    return re.search(pattern, password)

username = input("Masukkan username: ")
if not validate_username(username):
    print("Username tidak valid!")
else:
    email = input("Masukkan email: ")
    if not validate_email(email):
        print("Email tidak valid. Registrasi gagal!")
    else:
        password = input("Masukkan password: ")
        if not validate_password(password):
            print("Password tidak valid! Panjang minimal 8 karakter, harus mengandung huruf kapital, huruf kecil, dan angka. Simbol tidak diperbolehkan.")
        else:
            print(f"Registrasi berhasil! Selamat datang, {username}!")