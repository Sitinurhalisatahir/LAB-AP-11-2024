import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" 
    return re.search(pattern, username) 

def is_valid_email (email):
    pattern = r"^[a-z]+\d{0,}\@[a-z]+\.(com|co\.id)$" 
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z\d]{8,}$" 
    return re.search(pattern, password)

username = input("Masukkan username: ") 
if is_valid_username(username):
    email = input("Masukkan email: ") 
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print(f"\n Halo {username} Registrasi anda berhasil!")
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")