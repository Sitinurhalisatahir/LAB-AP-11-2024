def teka_teki():
    try:
        n = int(input("Masukkan angka: "))
        
        if n <= 0:
            print("Input tidak Valid")
            return
        
        langkah = 0  
        
        while n != 1:
            print(float(n))  
            if n % 2 == 0:  
                n //= 2
            else:           
                n *= 3 + 1
            langkah += 1   
        
        print(float(n)) 
        print(f"Jumlah langkah: {langkah}")  
        
    except ValueError:
        print("Input tidak Valid")  

teka_teki()
