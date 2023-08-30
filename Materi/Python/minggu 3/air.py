def air ():
    # Program Kondisi Air
    # Spesifikasi : Kondisi air
    
    # KAMUS
    #   t : int
    
    # ALGORITMA
    t = int(input("Masukkan suhu: "))
    
    if(t<0):
        return "PADAT"
    elif(0<t<100):
        return "CAIR"
    elif(t>100):
        return "GAS"
    elif(t==0):
        return "ANTARA PADAT-CAIR"
    else:
        return "ANTARA CAIR-GAS"
print(f"Output : {air()}")