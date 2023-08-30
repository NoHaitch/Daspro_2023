# KAMUS
# 	a, b : char

# ALGORITMA

a = input()
b = input()

if((not a.isupper()) or (not b.isupper())):
	print("Tidak valid")
else:
	if(ord(a)-ord(b) < 0):
		if(ord(b)-ord(a) < (ord(a)-ord(b)+26)):
			print(ord(b)-ord(a))
		else:
			print(ord(a)-ord(b)+26)
	else:
		if(ord(a)-ord(b) < (ord(b)-ord(a)+26)):
			print(ord(a)-ord(b))
		else:
			print(ord(b)-ord(a)+26)