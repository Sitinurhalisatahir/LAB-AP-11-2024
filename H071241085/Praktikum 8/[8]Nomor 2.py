import re

def validate_ip(ip):
    """
    Memvalidasi apakah alamat IP yang diberikan adalah IPv4, IPv6, atau bukan keduanya.

    Pola Validasi:
    1. **IPv4**:0
       - `^((\d|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(\d|[0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`
       - Mengharuskan alamat IPv4 yang terdiri dari empat bagian desimal, masing-masing dipisahkan oleh titik.
       - Setiap bagian bernilai dari 0 hingga 255:
         - `\d` menangkap satu digit (0-9).
         - `[0-9]{2}` menangkap dua digit.
         - `1[0-9]{2}` menangkap tiga digit angka dari 100 hingga 199.
         - `2[0-4][0-9]` menangkap tiga digit angka dari 200 hingga 249.
         - `25[0-5]` menangkap nilai 250 hingga 255.
       - `{3}` digunakan untuk mengulangi tiga bagian yang diakhiri titik, dan bagian keempat diakhiri oleh `$`.

    2. **IPv6**:
       - `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`
       - Mengharuskan alamat IPv6 yang terdiri dari delapan bagian heksadesimal (0-9, a-f, A-F), masing-masing dipisahkan oleh titik dua.
       - Setiap bagian memiliki panjang dari 1 hingga 4 karakter, diakhiri oleh `$`.

    Parameter:
    - `ip`: string alamat IP yang ingin divalidasi.

    Return:
    - Mengembalikan "IPv4" jika alamat IP adalah IPv4 yang valid, "IPv6" jika alamat IP adalah IPv6 yang valid, atau
      "Bukan IP Address" jika tidak valid.

    """
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