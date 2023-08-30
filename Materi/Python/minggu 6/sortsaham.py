def sort(arr,lenght):
    for index_awal in range(lenght//3):
        max = int(arr[index_awal][0])
        iMax = index_awal
        for i in range(index_awal+1,lenght//3):
            if(int(arr[i][0]) > max):
                iMax = i
                max = int(arr[i][0])
        temp = arr[index_awal]
        arr[index_awal] = arr[iMax]
        arr[iMax] = temp
    return arr


path = input("Nama file : ")
with open("minggu 6/"+path,"r") as file: #minggu 6 karena console di parent direktori/ ngga langsung di dalem file utama dirunnya
    i = 0
    count = 0
    f = file.readlines()
    while True:
        if(f[i] == "99999999"):
            break
        else:
            count += 1
        i += 1
    data = [[0,"",""] for _ in range(count// 3)]
    index = 0
    last_row = False
    for i in range(count):
        if(i % 3 == 0):
            data[index][0] = f[i][:-1]
        elif( i % 3 == 1):
            data[index][1] = f[i][:-1]
        else:
            data[index][2] = f[i][:-1]
            index += 1
    data = sort(data,count)
    for i in range(count//3-1,-1,-1):
        first_data = True
        for j in range(3):
            if(first_data):
                first_data = False
            else :
                print(",",end="")
            print(data[i][j],end="")
        print()

