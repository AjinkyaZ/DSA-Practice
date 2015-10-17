def maxset(A):
    max_now = 0
    max_end = 0
    print A
    print len(A)
    subarr = []
    sum_curr = 0
    max_sum = 0
    for i in xrange(1, len(A)):
        x = A[i]
        if x >= 0:
            max_sum = max(x, max_sum + x)
            sum_curr = max(sum_curr, max_sum)
        else:
            sum_curr = 0
        return sum_curr

            
            
        

A = input("enter\n")
print maxset(A)
