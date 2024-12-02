def akronim(a):

    words = a.split()
    akronim = ''.join([word[0].upper() for word in words])
    return akronim

kalimat = "saya makan"
print(akronim(kalimat))  