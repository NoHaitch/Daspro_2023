def cariBilangan ():
    # Program Cari Bilangan
    # Spesifikasi : Mencari bilangan 
    
    # KAMUS
    #   t : int
    
    # ALGORITMA
    valid = False
    while valid == False:
        n = int(input("Masukkan n: "))
        if(0<n<=100):
            valid = True
        else:
            print("Masukkan salah. Ulangi!")
    num = []
    for i in range(n):
        num.append(int(input(f"bilangan ke-{i+1}: ")))
    x = int(input("Masukkan x: "))
    if(x<-1 or x>1):
        print("Tidak diproses")
    else:
        res = -1
        for i in range(n):
            if(x == 0):
                if(num[i]==0):
                    res = i+1
                    break
            elif(x==-1):
                if(num[i]<0):
                    res = i+1
                    break
            elif(x==1):
                if(num[i]>0):
                    res = i+1
                    break
        if(res == -1):
            if(x==0):
                print("Tidak ada 0")
            elif(x==-1):
                print("Tidak ada negatif")    
            else:
                print("Tidak ada positif")
        else:
            print(f"Ditemukan di urutan {res}")
cariBilangan()