def gcd(a,b):
	if a<0:
		raise ValueError
	if b<0:
		raise ValueError
	if not( (type(a) is int) or (type(a) is long) ):
		raise TypeError
	if not( (type(b) is int) or (type(b) is long) ):
		raise TypeError
	if b==0:
		return a
	return gcd(b,a%b)
