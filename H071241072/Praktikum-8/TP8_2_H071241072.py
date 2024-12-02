import re

def check_ip_address(ip):
    ipv4_pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    '''
    Format IPv4:
    - Empat kelompok angka (oktet) yang dipisahkan oleh titik (`.`).
    - Setiap kelompok terdiri dari 1 hingga 3 digit angka, dengan rentang nilai antara 0 hingga 255.

    Pola regex:
    - `[0-9]{1,3}`: Memungkinkan setiap kelompok terdiri dari angka 1 hingga 3 digit (misalnya `1`, `192`, `255`).
    - `\.`: Memungkinkan setiap kelompok terdiri oleh titik.
    - `{3}`: Menyatakan bahwa kelompok `[0-9]{1,3}\.` diulang tiga kali, untuk mencocokkan tiga oktet pertama dari alamat IPv4.
    - `[0-9]{1,3}`: Oktet keempat yang juga terdiri dari 1 hingga 3 digit angka.
    '''
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}$'
    '''
    Format IPv6:
    - Delapan kelompok heksadesimal yang dipisahkan oleh titik dua (`:`).
    - Setiap kelompok terdiri dari 1 hingga 4 karakter heksadesimal (0-9 atau a-f/A-F).
    
    Pola regex:
    - `[0-9a-fA-F]{1,4}`: Setiap kelompok terdiri dari 1 hingga 4 karakter heksadesimal (misalnya `2001`, `0db8`, `85a3`).
    - `\:`: Memungkinkan setiap kelompok terdiri oleh titik dua.
    - `{7}`: Menyatakan bahwa kelompok `[0-9a-fA-F]{1,4}:` diulang tujuh kali, untuk mencocokkan tujuh kelompok  pertama dari alamat IPv6.
    - `[0-9a-fA-F]{1,4}`: Kelompok kedelapan yang juga terdiri dari 1 hingga 4 karakter heksadesimal.
    '''
    if re.match(ipv4_pattern, ip):
        parts = ip.split(".")
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"

    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

N = int(input("Masukkan jumlah baris: "))

for i in range(N):
    ip = input().strip()
    if len(ip) > 500:
        print("Karakter lebih dari 500")
    else:    
        print(check_ip_address(ip))