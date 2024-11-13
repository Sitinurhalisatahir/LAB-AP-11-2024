import re
def validate_ip_address(ip: str) -> str:
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'#8 kelompok karakter heksadesimal yang dipisahkan tanda titik dua
    
    if re.match(ipv4_pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    
    return "Neither"

def check_ip_addresses(N: int, ip_addresses: list):
    results = []
    for ip in ip_addresses[:N]:  
        results.append(validate_ip_address(ip.strip()))
    return results

try:
    N = int(input("Masukkan jumlah baris IP: "))
    ip_addresses = [input(f"IP address {i+1}: ") for i in range(N)]
    results = check_ip_addresses(N, ip_addresses)

    for result in results:
        print(result)

except:
    print("Masukkan integer sadjah")






    


