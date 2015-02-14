from gcd import gcd

def test_gcd():
	assert gcd(48, 72)==24 , "fails---gcd(48, 72) != 24"
	assert gcd(12, 13)==1,"fails---gcd(12, 13)!=1"

	flag=0
	try:
		gcd(-1,5)
	except ValueError:
		flag=1
	assert flag==1,"ValueError not catched gcd(-1,5)"

	flag=0
	try:
		gcd(1,-5)
	except ValueError:
		flag=1
	assert flag==1,"ValueError not catched gcd(1,-5)"

	flag=0
	try:
		gcd(-10,-5)
	except ValueError:
		flag=1
	assert flag==1,"ValueError not catched gcd(-10,-5)"

	flag=0
	try:
		gcd(1,0.5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd(1,0.5)"

	flag=0
	try:
		gcd(1,"sdf")
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd(1,'sdf')"

	flag=0
	try:
		gcd(1.0,5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd(1.0,5)"

	flag=0
	try:
		gcd(1.0,'a')
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd(1.0,'a')"

	flag=0
	try:
		gcd('sdfklaldf',5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd('sdfklaldf',5)"

	flag=0
	try:
		gcd('sdfklaldf',5.0)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched gcd('sdfklaldf',5.0)"
	
	print "gcd() passed all tests!"
if __name__ == "__main__":
	test_gcd()