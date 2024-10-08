import random

def Kartu():
    kartu = random.randint(2, 11)
    return kartu

def blackjack():
    print("Welcome to Blackjack!")
    
    kartu_pemain = Kartu()
    kartu_dealer = Kartu()
    
    print(f"Kartu anda sekarang adalah: {kartu_pemain}")
    jawab = "y"
    
    while jawab == "y":
        jawab = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if jawab == 'y':
            kartu_baru = Kartu()
            kartu_pemain += kartu_baru
            print(f"Kartu anda sekarang adalah: {kartu_pemain}")
            if kartu_pemain > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif jawab == 'n':
            break
    
    print(f"Kartu dealer adalah: {kartu_dealer}")
    while kartu_dealer < 17:
        kartu_baru = Kartu()
        kartu_dealer += kartu_baru
        print(f"Kartu dealer sekarang adalah: {kartu_dealer}")
    
    if kartu_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif kartu_pemain > kartu_dealer:
        print("Anda menang!")
    elif kartu_pemain == kartu_dealer:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()