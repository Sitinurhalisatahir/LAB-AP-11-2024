def generate_substrings(s):
  substrings = [] #list masih kosong
  for sub_len in range(1, len(s) + 1): #menentukan panjang substring dari string s, mulai dari panjang terkecil (1) hingga panjang terbesar 
    for start_index in range(len(s) - sub_len + 1): #Loop kedua menghasilkan: range(len(s) - 2 + 1) → range(4) → menghasilkan indeks 0, 1, 2, 3. Substring yang dihasilkan: "HE", "EL", "LL", "LO".
      substrings.append(s[start_index:start_index + sub_len]) 
  return substrings 

# Get input from the user
input_string = input("Input your string: ")

# Generate and print all substrings
substrings = generate_substrings(input_string)
for substring in substrings: #substrings berisi ['HE', 'EL', 'LL', 'LO'] Pada iterasi pertama, substring akan menjadi 'HE
  print(substring)