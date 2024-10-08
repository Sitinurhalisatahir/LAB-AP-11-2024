import random

def tarik_kartu():
    return random.randint(1,11)

def blackjack():
    print('Welcome to Blackjack!')

    kartu_player = tarik_kartu()
    print(f'Kartu anda sekarang adalah {kartu_player}')

    while True:
        player = input('Apakah masih akan mengambil kartu? (y/n): ').lower()
        if player == 'y':
            kartu_player += tarik_kartu()
            print(f'Kartu anda sekarang adalah :{kartu_player}')

            if kartu_player > 21:
                print('Player kalah! kartu player melebihi 21')
                return
        else:
            break

    #dealer
    kartu_dealer = tarik_kartu()
    print(f'Kartu dealer adalah: {kartu_dealer}')

    while kartu_dealer < 17:
        kartu_dealer += tarik_kartu()
        print(f'Kartu dealer sekarang adalah: {kartu_dealer}')

    if kartu_dealer > 21 or kartu_player > kartu_dealer:
        print('Player menang! kartu player melebihi kartu dealer')
    elif kartu_player == kartu_dealer:
        print('Seri!')
    else:
        print('Player kalah! kartu dealer melebihi kartu player')

blackjack()