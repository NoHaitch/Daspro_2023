# Nama : Raden Francisco Trianto Bratadiningrat	
# NIM : 19622078
# Tanggal : 15 Maret 2023

# Program
# Spesifikasi

# KAMUS

# ALGORITMA
n = int(input())
if(0<n<=50):
	num = [0 for _ in range(n)]
	for i in range(n):
		num[i] = int(input())
	a = int(input())

# cari minimum total
	mintot = 301 #karena isi array pasti -100<z<100
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if(num[i]+num[j]+num[k] > a):
					if(num[i]+num[j]+num[k]-a < mintot):
						mintot = num[i]+num[j]+num[k]-a
				else:
					if(a-(num[i]+num[j]+num[k]) < mintot):
						mintot = a-(num[i]+num[j]+num[k])
	res = 0
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if(num[i]+num[j]+num[k] > a):
					if(num[i]+num[j]+num[k]-a == mintot):
						res += 1
				else:
					if(a-(num[i]+num[j]+num[k]) == mintot):
						res += 1
	print(res)
else:
	print("Tidak valid")
