def printspiral(A, m, n):

    print "rows -->" , m
    print "columns -->", n
    print "2d array --> \n"
    for x in xrange(m):
        print A[x]
    t = 0
    b = m-1
    l=0
    r=n-1
    dir = 0
    ret = []
    while (l<=r and t<=b):
        if dir == 0:
            print "left to right"
            for i in xrange(l,r+1):
                print A[t][i]
                ret.append(A[t][i])
            t=t+1
            print ""
        elif dir == 1:
            print "top to bottom"
            for i in xrange(t,b+1):
                print A[i][r]
                ret.append(A[i][r])
            r=r-1
            print ""
        elif dir == 2:
            print "right to left"
            for i in xrange(r,l-1,-1):
                print A[b][i]
                ret.append(A[b][i])
            b=b-1
            print ""
        elif dir == 3:
            print "bottom to top"
            for i in xrange(b,t-1,-1):
                print A[i][l]
                ret.append(A[i][l])
            l=l+1
            print ""
        #change direction
        dir = (dir+1)%4

    return ret




# longer array for testing
#m = 4; n = 4
#A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m = 3; n = 3
A=[[1,2,3],[4,5,6],[7,8,9]]
#m=4; n=2
#A = [[1,2],[3,4],[5,6],[7,8]]
#m = 2; n= 3
#A = [[1,2,3],[4,5,6]]
x = printspiral(A, m, n)
print x
