def beasiswa():
    # Program Beasiswa
    # Spesifikasi : Menentukan kategori beasiswa dari ketentuan yang diberikan
    
    # KAMUS
    #   ip, pot : Float
    
    # ALGORITMA
    ip = float(input("Masukkan ip : "))
    pot = float(input("Pendapatan orang tua : "))
    if(ip >= 3.5):
        return 4
    elif (ip<3.5 and pot<1):
        return 1
    elif (ip<3.5 and 1<= pot < 5):
        if(ip>=2):
            return 3
        else:
            return 2
    else:
        return 0
print(f"Output : {beasiswa()}")