# KAMUS
# 	n,i,j,x : int
# 	arr : array of integer
# 	cek : bool

# ALGORITMA

arr = []
while True:
	n = int(input())
	if (n == -9999):
		break
	else:
		arr.append(n)
x = 1
while True:
	if(x in arr):
		x += 1
		continue
	else:
		cek = True
		for i in range(len(arr)):
			if(cek == False):
				break
			for j in range(i+1,len(arr)):
				if(arr[i]+arr[j] == x):
					cek = False
					break
		if(cek == True):
			print(x)
			break
		else:
			x += 1