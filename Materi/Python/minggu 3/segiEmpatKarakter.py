def segiEmpatKarakter ():
    # Program Segi Empat Karakter
    # Spesifikasi : menggambar Segi Empat Karakter c1 sebagai bingkai dan c2 sebagai isi dengan panjang n
    
    # KAMUS
    #   c1, c2 : char
    #   n : int
    
    # ALGORITMA
    n = int(input("Masukkan panjang sisi: "))
    c1 = input("Masukkan c1: ")
    c2 = input("Masukkan c2: ")
    print("Output : ")
    if(n<=0 or c1==c2):
        print("Masukkan tidak valid")
    else:
        for i in range(n):
            if(i==0 or i==n-1):
                for j in range(n):
                    print(c1,end="")
                print()
            else:
                for j in range(n):
                    if(j==0 or j==n-1):
                        print(c1,end="")
                    else:
                        print(c2,end="")
                print()
segiEmpatKarakter()