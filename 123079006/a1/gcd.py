def gcd(a,b):
#sanity checks
	if a<0 or b<0:
		raise ValueError
	if not(type(a) in [int ,   long ] and type(b) in [int, long ]):
		raise TypeError

#GCD calculation
	if a == 0:
		return b
	while b != 0:
		if a > b:
			a = a - b
		else:
			b = b - a
	return a
