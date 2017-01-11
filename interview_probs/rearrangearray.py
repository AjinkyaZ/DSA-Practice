def rearrangeArray(A):
    print "before", A
    x = len(A)
    for i in xrange(0,x):
        A[i] = (A[A[i]]%x)*x
        print A[i]

    for i in xrange(0,x):
        A[i] = int(A[i]/x)
        print A[i]
    print "after", A





A = input("Enter array\n")
rearrangeArray(A)
