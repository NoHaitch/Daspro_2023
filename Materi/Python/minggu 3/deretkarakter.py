def deretkarakter():
    # Program Deret Karakter
    # Spesifikasi : menuliskan satu baris sepanjang n dan berisi karakter x
    
    # KAMUS
    #   n : int
    #   x : Char

    # ALGORITMA
    x = input("Masukkan karakter: ")
    n = int(input("Masukkan panjang: "))
    print("OUTPUT: ",end="")
    for i in range(n):
        print(x,end="")
    print()
deretkarakter()