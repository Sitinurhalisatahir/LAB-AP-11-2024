import re

s = str(input("Masukkan string : "))
pattern = r"[A-Za-z02468]{40}[13579\s]{5}"

result = re.match(pattern, s)

if result:
    print(True)
else:
    print(False)