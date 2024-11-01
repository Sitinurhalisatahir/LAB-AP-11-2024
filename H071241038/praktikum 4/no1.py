# import random

# # Fungsi untuk menghitung nilai kartu
# def hitung_nilai_kartu(kartu):
#     total = 0
#     jumlah_ace = 0
#     for k in kartu:
#         if k in ['J', 'Q', 'K']:
#             total += 10
#         elif k == 'A':
#             total += 11
#             jumlah_ace += 1
#         else:
#             total += k
#     # Menyesuaikan nilai As jika total melebihi 21
#     while total > 21 and jumlah_ace:
#         total -= 10
#         jumlah_ace -= 1
#     return total

# # Fungsi untuk menarik kartu secara acak
# def ambil_kartu():
#     kartu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
#     return random.choice(kartu)

# # Fungsi permainan Blackjack
# def main_blackjack():
#     print("Welcome to Blackjack!")
    
#     # Kartu pemain dan dealer
#     kartu_pemain = [ambil_kartu()]
#     kartu_dealer = [ambil_kartu()]
    
#     # Menampilkan kartu awal pemain dan dealer
#     print(f"Kartu anda sekarang adalah: {kartu_pemain}")
#     print(f"Kartu dealer adalah: [{kartu_dealer[0]}]")
    
#     # Pemain memilih untuk mengambil kartu atau tidak
#     while True:
#         total_pemain = hitung_nilai_kartu(kartu_pemain)
#         if total_pemain > 21:
#             print("Anda kalah, kartu anda melebihi 21.")
#             return
        
#         ambil_kartu_lagi = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
#         if ambil_kartu_lagi == 'y':
#             kartu_pemain.append(ambil_kartu())
#             print(f"Kartu anda sekarang adalah: {kartu_pemain}")
#         elif ambil_kartu_lagi == 'n':
#             break
#         else:
#             print("Input tidak valid, silakan masukkan 'y' atau 'n'.")
    
#     # Dealer menarik kartu
#     while hitung_nilai_kartu(kartu_dealer) < 17:
#         kartu_dealer.append(ambil_kartu())
#         print(f"Kartu dealer sekarang adalah: {kartu_dealer}")
    
#     total_dealer = hitung_nilai_kartu(kartu_dealer)
#     total_pemain = hitung_nilai_kartu(kartu_pemain)
    
#     # Menentukan pemenang
#     if total_pemain > 21:
#         print("Anda kalah, kartu anda melebihi 21.")
#     elif total_dealer > 21:
#         print("Anda menang, dealer melebihi 21.")
#     elif total_pemain > total_dealer:
#         print("Anda menang!")
#     elif total_pemain == total_dealer:
#         print("Seri!")
#     else:
#         print("Dealer menang!")

# # Menjalankan permainan
# main_blackjack()

# import random

# # Fungsi untuk menarik kartu secara acak
# def draw_card():
#     cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Nilai kartu, As bernilai 11
#     return random.choice(cards)

# # Fungsi untuk menghitung total kartu, dengan memperhitungkan As (bisa 1 atau 11)
# def calculate_total(cards):
#     total = sum(cards)
#     while total > 21 and 11 in cards:
#         cards[cards.index(11)] = 1  # Mengganti As menjadi 1 jika total lebih dari 21
#         total = sum(cards)
#     return total

# # Fungsi utama permainan Blackjack
# def play_blackjack():
#     print("Welcome to Blackjack!")
    
#     # Pemain dan dealer memulai dengan satu kartu
#     player_cards = [draw_card()]
#     dealer_cards = [draw_card()]
    
#     print(f"Kartu anda: {player_cards[0]}")
#     print(f"Kartu dealer: {dealer_cards[0]}")

#     # Pemain mengambil kartu hingga berhenti atau total lebih dari 21
#     while calculate_total(player_cards) <= 21:
#         choice = input("Apakah Anda ingin mengambil kartu lagi? (y/n): ").lower()
#         if choice == 'y':
#             player_cards.append(draw_card())
#             print(f"Kartu anda sekarang: {calculate_total(player_cards)}")
#         else:
#             break

#     # Cek jika pemain langsung kalah karena lebih dari 21
#     if calculate_total(player_cards) > 21:
#         print("Anda kalah, kartu Anda melebihi 21.")
#         return

#     # Dealer mengambil kartu hingga totalnya minimal 17
#     while calculate_total(dealer_cards) < 17:
#         dealer_cards.append(draw_card())

#     print(f"Kartu dealer sekarang: {calculate_total(dealer_cards)}")

#     # Menentukan pemenang
#     player_total = calculate_total(player_cards)
#     dealer_total = calculate_total(dealer_cards)
    
#     if dealer_total > 21:
#         print("Anda menang, dealer melebihi 21.")
#     elif player_total > dealer_total:
#         print("Anda menang!")
#     elif player_total < dealer_total:
#         print("Dealer menang!")
#     else:
#         print("Seri!")

# # Menjalankan permainan
# play_blackjack()

import random

def tarik_kartu():
    kartu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  
    return random.choice(kartu)

# Fungsi untuk menghitung total kartu, dengan memperhitungkan As (bisa 1 atau 11)
def hitung_total(kartu):
    total = sum(kartu)
    while total > 21 and 11 in kartu:
        kartu[kartu.index(11)] = 1  # Mengganti As menjadi 1 jika total lebih dari 21
        total = sum(kartu)
    return total

def mainkan_blackjack():
    print("Selamat datang di Blackjack!")
    kartu_pemain = [tarik_kartu()]
    kartu_dealer = [tarik_kartu()]
    print(f"Kartu anda: {kartu_pemain[0]}")
    print(f"Kartu dealer: {kartu_dealer[0]}")

    # Pemain mengambil kartu hingga berhenti atau total lebih dari 21
    while hitung_total(kartu_pemain) <= 21:
        pilihan = input("Apakah Anda ingin mengambil kartu lagi? (y/n): ")
        if pilihan == 'y':
            kartu_pemain.append(tarik_kartu())
            print(f"Kartu anda sekarang: {hitung_total(kartu_pemain)}")
        elif pilihan == 'n':
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 'n'.")

    if hitung_total(kartu_pemain) > 21:
        print("Anda kalah, kartu Anda melebihi 21.")
        return

    while hitung_total(kartu_dealer) < 17:
        kartu_dealer.append(tarik_kartu())

    print(f"Kartu dealer sekarang: {hitung_total(kartu_dealer)}")

    # Menentukan pemenang
    total_pemain = hitung_total(kartu_pemain)
    total_dealer = hitung_total(kartu_dealer)
    
    if total_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif total_pemain > total_dealer:
        print("Anda menang!")
    elif total_pemain < total_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

mainkan_blackjack()
