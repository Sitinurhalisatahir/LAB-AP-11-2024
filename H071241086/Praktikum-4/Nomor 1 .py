
import random

def draw_card():
    """Mengambil kartu secara acak dengan nilai 1-11."""
    return random.randint(1, 11)

def calculate_total(cards):
    """Menghitung total nilai dari kartu, dengan mempertimbangkan As."""
    total = sum(cards)
    aces_count = cards.count(1)  #untuk menghitung jumlah As yang ada di kartu

    # ubah nilai As dari 1 menjadi 11 jika tidak melebihi 21
    while total + 10 <= 21 and aces_count:
        total += 10
        aces_count -= 1
    
    return total

def play_blackjack():
    print("Welcome to Blackjack!")
    
    player_cards = [draw_card(), draw_card()]  # Dua kartu awal untuk pemain
    dealer_cards = [draw_card()]  # Satu kartu untuk dealer
    
    print(f"Kartu anda: {player_cards}, Total: {calculate_total(player_cards)}")
    
    # Giliran pemain
    while True:
        choice = input("Ambil kartu? (y/n) ").strip().lower()
        
        if choice == 'y':
            player_cards.append(draw_card())
            total_player = calculate_total(player_cards)
            print(f"Kartu anda: {player_cards}, Total: {total_player}")
            if total_player > 21:
                print("Anda kalah, kartu melebihi 21.")
                return
        elif choice == 'n':
            break

    # Giliran dealer
    total_dealer = calculate_total(dealer_cards)
    print(f"Kartu dealer: {dealer_cards}, Total: {total_dealer}")
    
    while total_dealer < 17:
        dealer_cards.append(draw_card())
        total_dealer = calculate_total(dealer_cards)
        print(f"Kartu dealer: {dealer_cards}, Total: {total_dealer}")

    # Menentukan hasil
    print(f"Hasil akhir - Anda: {calculate_total(player_cards)}, Dealer: {total_dealer}")
    
    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif calculate_total(player_cards) > total_dealer:
        print("Anda menang!")
    elif calculate_total(player_cards) < total_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

# Mulai permainan
play_blackjack()



