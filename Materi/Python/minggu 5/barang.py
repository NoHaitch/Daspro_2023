# KAMUS
#   n, i : int
#   harga : array of int
#   res : int

n = int(input("Jumlah Barang: "))
harga = [0 for _ in range(n)]
for i in range(n):
    harga[i] = int(input(f"{i+1}: "))
res = 0
for i in harga:
    res += i
print(res)