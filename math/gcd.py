#euclidean method to calculate gcd
def gcd(a, b):
	x = a%b
	i=1
	while b > 0:
		x = b
		b = a%b
		a = x
        return a

#binary method to calculate gcd
def binarygcd(a, b):
	if a == 0 or b == 0:
		if a>b:
			return a
		else:
			return  b
	else:
		while(b):
			a = a%b
			b = b^a
			a = a^b
			b = b^a
		return a

a = input("enter 2 numbers\n")
b = input()
print a, b
print "gcd by euclidean method :", gcd(a, b)
print "gcd by binary method:", binarygcd(a, b)
