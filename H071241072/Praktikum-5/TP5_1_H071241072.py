def palindrom():

    string = input("Masukkan sebuah kata atau kalimat: ").lower()
    reverse = ''.join(reversed(string))

    if string == reverse:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

palindrom()