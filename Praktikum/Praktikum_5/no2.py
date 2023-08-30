# KAMUS
# 	n,i,j : int
# 	a, key, value, mx : array of integer

# ALGORITMA

n = int(input())
a = list(map(int, input().strip().split()))
key = []
value = []
for i in a:
	if (i in key):
		for j in range(len(key)):
			if(key[j] == i):
				index = j
				break
		value[index] += 1
	else:
		key.append(i)
		value.append(1)	
count = 0
for i in range(len(value)):
	if(value[i] == max(value)):
		count += 1
mx = []
for i in range(len(value)):
	if(value[i] == max(value)):
		mx.append(key[i])
print(min(mx))