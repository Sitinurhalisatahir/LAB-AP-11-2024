import re

def is_valid_username(username):
    """
    Memvalidasi apakah username sesuai dengan aturan berikut:
    - Panjangnya antara 5 hingga 20 karakter.
    - Harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu digit.
    - Hanya berisi huruf (A-Z, a-z) dan angka (0-9).

    Pola regex:
    - `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{5,20}$`
        - `(?=.*[a-z])`: Memastikan setidaknya ada satu huruf kecil.
        - `(?=.*[A-Z])`: Memastikan setidaknya ada satu huruf besar.
        - `(?=.*\d)`: Memastikan setidaknya ada satu digit.
        - `[A-Za-z0-9]{5,20}`: Mengatur panjang karakter antara 5 hingga 20 karakter, hanya terdiri dari huruf dan angka.

    Parameter:
    - `username` (str): Username yang ingin divalidasi.

    Return:
    - Mengembalikan hasil pencocokan pola pada username atau `None` jika tidak valid.

    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)


def is_valid_email(email):
    """
    Memvalidasi apakah email sesuai dengan aturan berikut:
    - Panjang minimal 4 karakter sebelum tanda '@'.
    - Dimulai dengan huruf kecil atau angka.
    - Format email harus memiliki domain yang valid, diakhiri dengan ".com" atau ".co.id".

    Pola regex:
    - `^[a-z0-9]{4,}@[a-z0-9]+\.(com|co\.id)$`
        - `^[a-z0-9]{4,}`: Memastikan bagian awal terdiri dari huruf kecil atau angka dengan panjang minimal 4 karakter.
        - `@[a-z0-9]+`: Memastikan bagian domain berisi huruf kecil atau angka.
        - `\.(com|co\.id)$`: Memastikan domain diakhiri dengan `.com` atau `.co.id`.

    Parameter:
    - `email` (str): Email yang ingin divalidasi.

    Return:
    - Mengembalikan hasil pencocokan pola pada email atau `None` jika tidak valid.

    """
    pattern = r"^[a-z0-9]{4,}@[a-z0-9]+\.(com|co\.id)$"
    return re.search(pattern, email)


def is_valid_password(password):
    """
    Memvalidasi apakah password sesuai dengan aturan berikut:
    - Panjang minimal 8 karakter.
    - Harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu digit.

    Pola regex:
    - `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$`
        - `(?=.*[a-z])`: Memastikan setidaknya ada satu huruf kecil.
        - `(?=.*[A-Z])`: Memastikan setidaknya ada satu huruf besar.
        - `(?=.*\d)`: Memastikan setidaknya ada satu digit.
        - `[A-Za-z\d]{8,}`: Mengatur panjang minimum 8 karakter, hanya terdiri dari huruf dan angka.

    Parameter:
    - `password` (str): Password yang ingin divalidasi.

    Return:
    - Mengembalikan hasil pencocokan pola pada password atau `None` jika tidak valid.

    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(pattern, password)


username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")

    if is_valid_email(email):
        password = input("Masukkan password: ")

        if is_valid_password(password):
            print(f"\nRegistrasi berhasil! \nHalo {username}")
        else:
            print("\nPassword yang kamu input berisiko dihack. Registrasi gagal.")

    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")

else:
    print("\nInputan username tidak valid. Registrasi gagal!")