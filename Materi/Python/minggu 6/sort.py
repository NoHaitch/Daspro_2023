def get_max(arr,index_start):
    max = arr[index_start]
    for i in arr[index_start:]:
        if (i > max):
            max = i
    return max

def get_idx(arr,number):
    for i in range(len(arr)):
        if(number == arr[i]):
            return i

def swap(array,indeks_1,indeks_2):
    temp = array[indeks_1]
    array[indeks_1] = array[indeks_2]
    array[indeks_2] = temp
    return array

def sort(arr):
    for i in range(len(arr)):
        maxArr = get_max(arr, i)
        maxIdx = get_idx(arr, maxArr)
        swap(arr, i, maxIdx)
    print(arr)

N = int(input("masukkan n: "))
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = int(input(f"ke-{i+1}: "))
sort(arr)