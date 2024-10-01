import random

def main():
    print("Welcome to Blackjack!")
    kartu_pemain = random.randint(2, 11)
    kartu_dealer = random.randint(2, 11)

    while True:
        print(f"Kartu anda sekarang adalah: {kartu_pemain}")
        pilih = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if pilih == 'y':
            kartu_pemain += random.randint(2, 11)
            if kartu_pemain > 21:
                print(f"Kartu anda sekarang adalah: {kartu_pemain}")
                print("Anda kalah!")
                return
        elif pilih == 'n':
            break
        else:
            print("Input tidak valid.")

    print(f"Kartu dealer adalah: {kartu_dealer}")
    while kartu_dealer < 17:
        kartu_dealer += random.randint(2, 11)
        print(f"Kartu dealer sekarang adalah: {kartu_dealer}")

    if kartu_dealer > 21 or kartu_pemain > kartu_dealer:
        print("Anda menang!")
    elif kartu_pemain < kartu_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")
main()