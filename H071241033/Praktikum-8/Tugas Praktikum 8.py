import re

def SOAL_1():
    input_string = input("Please enter multiple characters: ")
    pattern = r'^[A-Za-z2468]{40}[13579\s]{5}$'
    result = re.search(pattern, input_string)
    if result:
        print("TRUE")
    else:
        print("FALSE")
# SOAL_1()

#___________________________________________________________________

def SOAL_2():
    def IP_check(i):
        IPv4 = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
        result_4 = re.search(IPv4,i)
        IPv6 = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|((([0-9a-fA-F]{1,4}:){1,7}|:):([0-9a-fA-F]{1,4}:){1,6}|::))$'
        result_6 = re.search(IPv6,i)
        if result_4:
            print("--> IPv4")
        elif result_6:
            print("--> IPv6")
        else:
            print("--> Not IP Address")
    print("=== IP ADDRESS CHECK PROGRAM ===")
    n = int(input("Masukkan jumlah baris input(n): "))
    for i in range(1,n+1):
        user_input = input(f"\nInput {i}: ")
        IP_check(user_input)
# SOAL_2()

# ___________________________________________________________________

def SOAL_3():
    def username_check(a):
        patternUNAME = r'^[A-Za-z\d]{5,20}$'
        return re.search(patternUNAME, a)
    def email_check(b):
        patternEMAIL = r'^[a-z]+([0-9]{2,})?@[a-z]+\.(com|co)$'
        return re.search(patternEMAIL, b)
    def password_check(c):
        patternPW = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        return re.search(patternPW, c)
        
    print('''
========= STEP INTO A VAST MAGICAL WORLD OF ADVENTURE =========
                Genshin Impact Account - Sign-up
''')
    while True:
        a = input("\nEnter username: ")
        if username_check(a):
            break
        else:
            print("Invalid username. Please try again.")
    while True:
        b = input("\nEnter email: ")
        if email_check(b):
            break
        else:
            print("Invalid email address. Please enter a valid email.")
    while True:
        c = input("\nEnter password: ")
        if password_check(c):
            print(f'''
\nSign-up successful! You can now log in and start your adventure.
============  Welcome to the vast world of Teyvat!  ============
''')
            break
        else:
            print("Password is too weak. Please choose a stronger password.")
# SOAL_3()