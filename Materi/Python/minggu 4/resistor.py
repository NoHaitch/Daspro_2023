def resistor ():
    # Program Resistor
    # Spesifikasi : menghitung resistansi total
    
    # KAMUS
    #   r1, r2, r3 : float
    #   k : Char
    #   valid : bool

    # ALGORITMA
    valid = False
    while valid==False:
        r1 = float(input("Masukkan r1: "))
        r2 = float(input("Masukkan r2: "))
        r3 = float(input("Masukkan r3: "))
        k = input("Masukkan pilihan: ")
        if(r1 <=0 or r2<= 0 or r3<= 0 or not(any(k==a for a in ["s","S","p","P"]))):
            print("Masukkan salah")
        else:
            valid = True
    if(k == "s" or k == "S"):
        return r1+r2+r3
    elif(k == "p" or k == "P"):
        return (r2*r3 + r1*r3 + r1*r2)/(r1*r2*r3)
    
print(f"Output: {resistor()}")