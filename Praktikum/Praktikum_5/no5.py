def getIndex(arr,key):
	for i in range(len(arr)):
		if(arr[i] == key):
			return i

arrmain = []
while True:
	n = int(input())
	if(n < 0):
		break
	else:
		arrmain.append(n)
arr0 = arrmain
while True:
	arr1 = arr0[:round(len(arr0)/2)]
	arr2 = arr0[round(len(arr0)/2):]
	if(sum(arr1) <= sum(arr2)):
		arr0 = arr1
	else:
		arr0 = arr2
	print(getIndex(arrmain,arr0[0]))
	if(len(arr0) == 1):
		print(arr0[0])
		break
		
