berat = []
while True:
    n = int(input())
    if(n == -999):
        break
    elif(30<=n<=200):
        berat.append(n)
if(len(berat) == 0):
    print("Data kosong")
else:
    b50 = 0
    b100 = 0
    total = 0
    for i in berat:
        total += i
        if(i<=50):
            b50 += 1
        elif(i >= 100):
            b100 += 1
    print(len(berat))
    print(b50)
    print(b100)
    print(round(total/len(berat)))