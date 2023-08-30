def themepark ():
    # Program Themepark
    # Spesifikasi : Menentukan Kategori Kendaraan yang layak
    
    # KAMUS
    #   t, b, k : Float
    
    # ALGORITMA
    t = int(input("Masukkan tinggi : "))
    b = int(input("Masukkan berat : "))
    k = int(input("Masukkan kategori kendaraan : "))

    if(t>100 and b<= 150):
        if(k == 1 or k == 0):
            return False
        else: 
            return True
    elif(t<= 100 and b<= 150):
        if(k == 1 or (b>30 and k==2)):
            return True
        else:
            return False
    elif(t<=100 and b>150 and k==2):
        return True
    elif(200<=t<100 and b>150 and (k==2 or k==3)):
        return True
    elif(k==0):
        return True
    else:
        return False
print(f"Output : {themepark()}")