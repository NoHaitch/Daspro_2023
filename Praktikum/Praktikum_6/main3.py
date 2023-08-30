def sort(arr):
	while True:
		cek_count = 0
		for i in range(len(arr)-1):
			if(arr[i] > arr[i+1]):
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
				break
			else:
				cek_count += 1
		if(cek_count == len(arr)-1):
			return arr

import tester
tester.start("input.csv")
file = open("input.csv", "r")
lines = file.readlines()[1:]
deret_umur = [0 for _ in range(len(lines))]
lulus = 0
for i in range(len(lines)):
	data = lines[i].split(",")
	nilai = int(data[3])
	deret_umur[i] = int(data[2])
	if(nilai > 75):
		lulus += 1
print(lulus)
print(sort(deret_umur)[1])
file.close()
tester.end("input.csv")
