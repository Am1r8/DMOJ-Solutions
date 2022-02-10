a=int(input())
for x in range(a):
	b=int(input())
	for y in range(b):
		c=b+y
		d=b-y
		primec=True
		primed=True
		for z in range(2,int(c**0.5)+1):
			if c%z==0:
				primec=False
				break
		if primec==True:
			for z in range(2,int(d**0.5)+1):
				if d%z==0:
					primed=False
					break
		if primed==True and primec==True:
			print(c,d)
			break