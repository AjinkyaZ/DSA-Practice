import sys
if len(sys.argv) == 3:
	print "Number of args :", len(sys.argv)
	print "arg list:"
        for arg in sys.argv:
                print str(arg)
        print "program name : ", str(sys.argv[0])
        res = int(sys.argv[1])+int(sys.argv[2])
        print "sum of args is ", res
elif len(sys.argv) < 3:
	print "Too few args. Only 2 args accepted"
else:
	print "Too many args. Only 2 args accepted"
 


