from gcd import gcd

def test_gcd():
	assert gcd(48, 72)==24
	assert gcd(12, 13)==1
if __name__ == "__main__":
	test_gcd()