inp = input("Taxa de scolarizare: ")
y = float(inp)

inp = input("Zile interziere: ")
o = float(inp)

while o>=0:
	x = (y*0.0004)+y
	y = x
	o = o-1

print("Suma totala de plata: ", y)