def acronym(s):
    # Memisahkan kata-kata dalam string
    words = s.split() # Membagi string s menjadi daftar kata-kata berdasarkan spasi
    
    # Mengambil huruf pertama dari setiap kata dan menggabungkannya
    akronim = ''.join(word[0].upper() for word in words) #Mengambi dari setiap kata dalam daftar words.
    
    print(akronim)

# Mengambil input dari pengguna
input_string = input("Masukkan kalimat: ")
acronym(input_string)