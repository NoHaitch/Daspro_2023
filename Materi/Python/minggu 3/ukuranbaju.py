def ukuranbaju():
    # Program Ukuran Baju
    # Spesifikasi : Menentukan Ukuran Baju dari tinggi dan berat
    # KAMUS
    #   t : int
    #   b : int
    # ALGORITMA
    t = int(input("Masukkan tinggi : "))
    b = int(input("Masukkan berat : "))
    if (t <= 150) :
        return 1
    elif(150<t<=170):
        if(b <= 80):
            return 2
        else :
            return 3
    elif(60<b<=80):
        return 3
    else:
        return 4
print(f"Output : {ukuranbaju()}")