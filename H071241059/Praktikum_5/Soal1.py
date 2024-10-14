def palindrome(kalimat):
        huruf = kalimat.lower()
        balik = (''.join(reversed(huruf)))
    
        if balik == huruf:
            print('Palindrome')
        else:
            print('Tidak Palindrome')

palindrome('Ibu Ratna Antar Ubi')