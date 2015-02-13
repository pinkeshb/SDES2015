from gcd import gcd

def test_gcd():
	assert gcd(48, 72)==24
	assert gcd(12, 13)==1

	flag=0
	try:
		gcd(-1,5)
	except ValueError:
		flag=1
	assert flag==1,"ValueError not catched"

	flag=0
	try:
		gcd(1,-5)
	except ValueError:
		flag=1
	assert flag==1,"ValueError not catched"

	flag=0
	try:
		gcd(1,0.5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched"

	flag=0
	try:
		gcd(1.0,5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched"

	flag=0
	try:
		gcd(1.0,'a')
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched"

	flag=0
	try:
		gcd('sdfklaldf',5)
	except TypeError:
		flag=1
	assert flag==1,"TypeError not catched"
	
	print "gcd passed all tests!"
if __name__ == "__main__":
	test_gcd()