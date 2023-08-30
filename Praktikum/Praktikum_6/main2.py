import tester
tester.start("output.txt")

file = open("output.txt", "w")
string = input()
count = 0
count_str = 0
count_vokal = [0 for _ in range(5)]
# count_vokal dalam format [a, i, u, e, o]
for char in string:
	if(char == "."):
		break
	elif(char == "a"):
		count_vokal[0] += 1
		count +=1
	elif(char == "i"):
		count_vokal[1] += 1
		count +=1
	elif(char == "u"):
		count_vokal[2] += 1
		count +=1
	elif(char == "e"):
		count_vokal[3] += 1
		count +=1
	elif(char == "o"):
		count_vokal[4] += 1
		count +=1
	count_str += 1
for i in count_vokal:
	file.write(str(i))
file.write("\n")
file.write(str(count))
file.write("\n")
if(string[:count_str]!=""):
	file.write(string[:count_str])
else:
	file.write("Tidak ada huruf")
file.close()

tester.end("output.txt")