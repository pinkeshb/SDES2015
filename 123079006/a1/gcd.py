def gcd(a,b):
	if a<0:
		raise ValueError
	if b<0:
		raise ValueError
	if not(type(a) in [int ,   long ] and type(b) in [int, long ]):
		raise TypeError
	if a == 0:
		return b
	while b != 0:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a
