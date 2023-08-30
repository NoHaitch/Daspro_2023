import tester
tester.start("input.txt")

# Membaca model dari sebuah file
# ALGORITMA
with open("input.txt", "r") as f:
	lines = f.readlines()
	layer = int(lines[0])
	if (layer < 1):	
		print("Jumlah layer: 0")
	else:
		print("Jumlah layer: ",layer)
		index_layer = 1
		for i in range(layer):
			print("Layer ke-",i+1)
			fungsi_aktivasi = lines[index_layer][:-1] # -1 agar tidak ada newline
			print("Fungsi aktivasi: ", fungsi_aktivasi)
			index_layer += 1
			nNeuron = int(lines[index_layer])
			index_layer += 1
			print("Jumlah neuron: ",nNeuron)
			neuron = ["" for _ in range(nNeuron*2)]
			for j in range(0,nNeuron*2,2):
				temp = lines[index_layer][:-1].split(" ")
				neuron[j] = temp[0]
				neuron[j+1] = temp[1]
				index_layer += 1
			print("Weight neuron:",neuron)
			bias = ["" for _ in range(nNeuron)]

			if(i != layer-1):
				bias = lines[index_layer][:-1].split(" ")
			else:
				bias = lines[index_layer].split(" ")
				
			print("Bias: ",bias)
			index_layer += 1


tester.end("input.txt")