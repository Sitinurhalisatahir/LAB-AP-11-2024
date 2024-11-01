jumlah_data = int(input("masukkan jumlah data yang anda gunakan: "))
penggunaan = input("apakah mayoritas penggunaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)?: ")
personal_bisnis = input("apakah anda pengguna personal atau bisnis?: ")

if jumlah_data < 10 and penggunaan == "off-peak" and personal_bisnis == "personal":
  print("paket yang sesuai: paket A")
elif 10 <= jumlah_data <= 50 and penggunaan == "peak" and personal_bisnis == "personal":
  print("paket yang sesuai: paket B")
elif jumlah_data > 50 and penggunaan == "peak" and personal_bisnis == "personal" == "bisnis":
  print("paket yang sesuai: paket C")
elif jumlah_data > 50 and penggunaan == "off-peak" and personal_bisnis == "bisnis":
  print("paket yang sesuai: paket D")
else:
  print("tidak ada paket yang sesuai")