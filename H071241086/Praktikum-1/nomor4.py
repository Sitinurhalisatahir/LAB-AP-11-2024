suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))

suhu_kelvin = suhu_celcius + 273.15
suhu_reamur = suhu_celcius * 4/5
suhu_fahrenheit = suhu_celcius * 9/5 + 32

print(f"Suhu dalam Kelvin: {suhu_kelvin: .2f} K")
print(f"Suhu dalam Reamur: {suhu_reamur:.2f} R")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit:.2f} F")
