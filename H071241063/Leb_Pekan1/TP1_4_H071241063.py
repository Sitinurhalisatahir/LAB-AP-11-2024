celsius = float(input("Masukkan Suhu dalam Celsius: "))

kelvin = int(celsius + 273.15)
reaumur = int(celsius * 4 / 5)
fahrenheit = int(celsius * 9 / 5 + 32)

print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Kelvin adalah : {kelvin}K")
print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Reaumur adalah : {reaumur}R")
print(f"Hasil konversi dari suhu {celsius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")



