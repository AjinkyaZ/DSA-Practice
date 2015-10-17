def largestNum(A):
    print A
    res = []
    A = sorted(A, reverse=True)
    print A
    ln = len(A)
    for i in xrange(ln):
        x = str(A[i])
        print "x", x
        if i+1==ln:
            y = '0'
        else:
            y = str(A[i+1])
        print "y", y
        z = compareNums(x,y)
        print "larger", z
        if z == x and x not in res and y not in res and x!= '0':
            res.append(x)
            res.append(y)
            print "res", res
        elif z == y and y not in res and x not in res and y!='0':
            res.append(y)
            res.append(x)
            print "res", res

        result = ''
    for i in xrange(len(res)):
        result = result+res[i]
    print "result",  int(result)



def compareNums(a,b):
    a = str(a)
    b = str(b)
    for i in xrange(len(b)):
        if int(a[i])>int(b[i]):
            return a
        elif int(a[i])<int(b[i]):
            return b
        else: continue
    
    if int(a[0])>int(b[0]):
        return a
    elif int(a[0])<int(b[0]):
        return b




A = input("enter array elements\n")
largestNum(A)
