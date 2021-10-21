inp = input("Ore lucrate: ")
o = int(inp)

inp = input("Salariu pe ora: ")
s = int(inp)

t = o*s

if o>40:
	ov = (o-40)*s*1.5
	t = t + ov
	print("Salariul: ", t)
	
else:
	print ("Salariul: ",t)