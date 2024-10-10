import random

def main():
    print("Welcome to Blackjack!")
    kartu_pemain = random.randint(1, 10)
    kartu_dealer = random.randint(1, 10)

    while True:
        print(f"Kartu anda sekarang adalah: {kartu_pemain}")
        pilih = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if pilih == 'n':
            break
        kartu_pemain += random.randint(1, 10)
        if kartu_pemain > 21:
            print(f"Kartu anda sekarang adalah: {kartu_pemain}")
            print("Anda kalah!")
            return

    while kartu_dealer < 17:
        kartu_dealer += random.randint(1, 10)

    print(f"Kartu dealer adalah: {kartu_dealer}")
    if kartu_dealer > 21 or kartu_pemain > kartu_dealer:
        print("Anda menang!")
    elif kartu_pemain < kartu_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

if __name__ == "__main__":
    main()







