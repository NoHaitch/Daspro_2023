# Nama : Raden Francisco Trianto Bratadiningrat	
# NIM : 19622078
# Tanggal : 15 Maret 2023

# Program Bilangan Berhubungan
# Spesifikasi : Mencari hubungan dari suatu array of integer terhadap bilangan bulat x

# KAMUS
# 	n,x : int
# 	jdekat, jjauh : int
# 	terdekat, terjauh : int
# 	ditemukan : Bool

# ALGORITMA
n = int(input())
x = int(input())
A = list(map(int, input("").split()))

# Jarak terdekat dan terjauh dari x
jdekat = max(A)
jjauh = 0
terdekat, terjauh = 0, 0
for i in A:
	if(i != n):
		if(n-i > 0):
			if(n-i < jdekat):
				jdekat = n-i
				terdekat = i
			if(n-i > jjauh):
				jjauh = n-i
				terjauh = i
		else:
			if(i-n < jdekat):
				jdekat = n-i
				terdekat = i
			if(i-n > jjauh):
				jjauh = n-i
				terjauh = i

# cari bilangan sama dengan x
ditemukan = False
for i in range(n):
	if(x in A and ditemukan == False):
		ditemukan = True
if(ditemukan == True):
	print(x)
	print(terdekat)
	print(terjauh,end="\n")
else:
	print("TIDAK ADA")
	print(terdekat)
	print(terjauh,end="\n")

