# Nama : Raden Francisco Trianto Bratadiningrat	
# NIM : 19622078
# Tanggal : 15 Maret 2023

# Program Saham
# Spesifikasi : Menentukan keuntungan maksimum dari membeli dan menjual saham jika diketahui harga saham n hari

# KAMUS
#	n, i, j : int
#	h : array of integer 
# 	hbeli, hjual : int
# 	untung : int

# ALGORITMA
n = int(input())
h = [0 for _ in range(n)]
for i in range(n):
	h[i] = int(input())
hbeli, hjual, untung = 0, 0, -1
for i in range(n):
	for j in range(i,n):
		if(h[j]-h[i] > untung):
			untung = h[j]-h[i]
			hbeli = i+1
			hjual = j+1
if(untung <= 0):
	print("Tidak beli")
else:
	print(untung)
	print(hbeli)
	print(hjual)
