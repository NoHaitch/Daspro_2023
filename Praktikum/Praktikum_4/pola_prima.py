# Nama : Raden Francisco Trianto Bratadiningrat	
# NIM : 19622078
# Tanggal : 15 Maret 2023

# Program Pola Prima
# Spesifikasi : Membuat persegi yang terbuat dari bilangan prima denga dimensi n x n

# KAMUS
#	n,i,j,x : int
# 	faktor : int
# 	prima : array of integer

# ALGORITMA
n = int(input())
prima = [0 for _ in range(n)]
x = 0
i = 1
while x < n:
	i+= 1
	faktor = 0
	for j in range(1,i+1):
		if(i%j == 0):
			faktor +=1
	if(faktor == 2):
		prima[x] = i
		x += 1
for i in range(n):
	for j in range(i,0,-1):
		print(prima[j],end=" ")
	for j in range(n-i):
		print(prima[j],end=" ")
	print()