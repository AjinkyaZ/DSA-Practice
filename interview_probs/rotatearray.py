def rotateArray(a,b):
	ret = []
	x = len(a)
	for i in xrange(len(a)):
                ret.append(a[(i + b)%x])
	return ret

a = input("enter a\n")
print a
b = input("enter b\n")
print b
x = rotateArray(a,b)
print x
