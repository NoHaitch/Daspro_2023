def konversisuhu ():
    # Program Konversi Suhu
    # Spesifikasi : Konversi suhu celcius menjadi tipe lainnya
    
    # KAMUS
    #   t : Float
    #   k : Char
    
    # ALGORITMA
    t = float(input("Masukkan suhu : "))
    k = input("konversi : ")

    if (k == "R"):
        return t * 4 / 5
    elif (k == "F"):
        return (t * 9 / 5) + 32
    else:
        return t + 273.15

print ("{:.2f}".format(konversisuhu()))
