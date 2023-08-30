n = int(input("Masukkan N: "))
while not(0<n<=100):
    print("Masukan salah. Ulangi!")
    n = int(input("Masukkan N: "))

char = ["" for _ in range(n)]
for i in range(n):
    char[i] = input(f"{i+1}: ")
cc = input("Masukkan cc: ")

if(cc == "S" or cc == "s"):
    for i in range(n):
        if(char[i].islower()):
            print(f"{i+1} {char[i]}")
            break
    else:
        print("Tidak ada huruf kecil")
elif(cc == "L" or cc == "l"):
    for i in range(n):
        if(char[i].isupper()):
            print(f"{i+1} {char[i]}")
            break
    else:
        print("Tidak ada huruf besar")
elif(cc == "X" or cc == "x"):
    for i in range(n):
        if(not char[i].isascii()):
            print(char[i])
            break
    else:
        print("Semua huruf")
else:
    print("Tidak diproses")
        
    