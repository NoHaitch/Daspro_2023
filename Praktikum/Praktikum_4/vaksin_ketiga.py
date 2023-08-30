# Nama : Raden Francisco Trianto Bratadiningrat	
# NIM : 19622078
# Tanggal : 15 Maret 2023

# Program Vaksin Ketiga
# Spesifikasi : Menentukan ketepatan waktu mendapatkan vaksin ketiga

# KAMUS
#	d : int
#	l : int
#	r : int

# ALGORITMA
d = int(input())
l = int(input())
r = int(input())

if(l<=d<=r):
	if((r-l)%2 == 1):
		if(d == ((r+l)/2)+0.5 or d == ((r+l)/2)-0.5):
			print("TUTUP")
		else:
			print("TEPAT")
	else:
		if(d == (r+l)/2):
			print("TUTUP")
		else:
			print("TEPAT")
elif(d<l):
	print("CEPAT")
else: #d>r
	print("TERLAMBAT")
	