def tobin(a):
	ret = []
	if a>1:
		tobin(a//2)
        x = a%2
        ret.append(x)
        for i in xrange(0, len(ret)):
                print ret[i],

a = input("Enter\n")
tobin(a)
