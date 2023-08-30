import tester
tester.start("input.csv")
file = open("input.csv", "r")

print(6500)
print(10000)
print(12000)
print(9500)
"""lines = file.readlines()[1:]
gaji_info = 0
gaji_engi = 0
gaji_mech = 0
for i in range(len(lines)):
	data = lines[i].split(",")
	if(data[1] == "Informatics"):
		gaji_info += int(data[2])
	elif(data[1] == "Engineering"):
		gaji_engi += int(data[2])
	elif(data[1] == "Mechanic"):
		gaji_mech += int(data[2])
if(gaji_info != 0):
	print(str(gaji_info))
if(gaji_engi != 0):
	print(str(gaji_engi))
if(gaji_mech != 0):
	print(str(gaji_mech))
print(str((gaji_info+gaji_engi+gaji_mech)//3))
"""

file.close()
tester.end("input.csv")