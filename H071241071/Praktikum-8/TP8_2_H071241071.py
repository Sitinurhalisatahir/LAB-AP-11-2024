import re

def validate_ip(ip):
    ipv4_pattern = r"^((\d|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(\d|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

    if re.match(ipv4_pattern, ip):
        return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

try:
    N = int(input("Masukkan jumlah IP: "))
    if N < 0:
        print("Masukkan angka positif")
    else:
        for i in range(N):
            ip = input("Masukkan IP: ")
            if len(ip) > 500:
                print("Karakter lebih dari 500")
            else:
                print(validate_ip(ip))

except ValueError:
    print("Input tidak valid")