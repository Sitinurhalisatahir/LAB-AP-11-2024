import random

def main():
    print("Welcome to Blackjack!")
    kartuPemain = random.randint(2,11)
    kartuDealer = random.randint(2,11)

   
    while True:
        print(f"Kartu anda sekarang adalah: {kartuPemain}")
        pilih = input("Ambil kartu lagi? (y/n): ").lower()
        if pilih == "y":
            kartuPemain += random.randint(2,11)
            if kartuPemain > 21:
                print(f"Kartu anda sekarang adalah: {kartuPemain}")
                print("Anda kalah")
                return
        elif pilih == "n":
            break
        else:
            print("Input Tidak Valid")
 
    while kartuDealer < 17:
        kartuDealer += random.randint(1,10)
    
 
    print(f"Kartu dealer adalah: {kartuDealer}")
    if kartuDealer > 21 or kartuPemain > kartuDealer:
        print("Anda menang")
    elif kartuPemain < kartuDealer:
        print("Dealer menang")
    else:
        print("Seri")


main()