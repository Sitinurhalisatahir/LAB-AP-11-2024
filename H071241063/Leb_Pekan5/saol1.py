def palindrome():
    string = input("Masukan Kalimat : ").lower()
    reversed_string = string[::-1]
    
    if string == reversed_string:
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome()

