def palindrome():
    a = input("Masukkan Kalimat atau Kata : ").lower()
    b = reversed(a)
    c = "".join(b)

    if a == c[::-1] :
        print("Palindrome")
    else :
        print("Not Palindrome")
palindrome()