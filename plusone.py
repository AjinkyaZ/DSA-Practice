def plusOne(A):
    print "start", A
    n = len(A)
    flag = 0
    for i in xrange(0, n):
        if A[i] != 9:
            flag = 0
            break
        else:
            flag = 1
    print"flag",  flag
    A[n-1] = A[n-1]+1
    for i in xrange(1, n+1):
        if(A[n-i]>9): 
                A[n-i] = 0
                A[n-i-1] = A[n-i-1] + 1
    if flag == 1:
        B = [i for i in xrange(n+1)]
        B[0] = 1
        for i in xrange(1, n+1):
            B[i] = A[i-1]
        B[n] = 0
        print "B", B
        return B
    return A

def PlusOneX(A):
        A[-1] += 1
        temp = 0
        tempSum = 0
        for i in range(len(A)-1,-1,-1):
    	    tempSum = A[i]+temp
    	    temp = (A[i]+temp)/10
    	    A[i] = tempSum%10
        if temp > 0:
    	    A = [temp] + A
        i = 0
        while i < len(A):
            if A[i] > 0:
                break
            i += 1
        return A[i:]



n = raw_input("enter number\n")
print int(n)
str_n = str(int(n))
print str_n
len_n = len(str_n)
print "len n --> : ", len_n
A = [i for i in xrange(len_n)]
for i in xrange(len_n):
    A[i] = int(str_n[i])
print A
print PlusOneX(A)
    
