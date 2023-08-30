n = int(input())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input(f"{i+1}: "))
x = int(input("x : "))
if(x in arr):
    maks, mins = False,False
    if(x == max(arr)):
        maks = True
        print("maksimum")
    if(x == min(arr)):
        min = True
        print("minimum")
    if(maks == False or min == False):
        print("N#A")
else:
    print(f"{x} tidak ada")