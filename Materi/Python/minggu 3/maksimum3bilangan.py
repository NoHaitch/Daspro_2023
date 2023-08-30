def maksimum3bilangan ():
    # Program Maksimum 3 Bilangan
    # Spesifikasi : menentukan bilangan terbesar dari 3 bilangan a, b, c
    
    # KAMUS
    #   a, b, c : int
    
    # ALGORITMA
    a = int(input("Masukkan bil ke-1: "))
    b = int(input("Masukkan bil ke-2: "))
    c = int(input("Masukkan bil ke-3: "))

    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
print(f"Output : {maksimum3bilangan()}")