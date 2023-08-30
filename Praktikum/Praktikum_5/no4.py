# KAMUS
# 	a, b : char

# ALGORITMA

def cekTerurut(n,arr):
	for i in range(n-1):
		if(arr[i] > arr[i+1]):
			return False
	return True

n = int(input())
a = list(map(int, input().strip().split()))
k = 0

while not cekTerurut(n,a):
	if(k > n):
		print("Tidak")
		break
	else:
		k += 1
		a = [a[n-1]] + a[:n-1]
else:
	print(k)	