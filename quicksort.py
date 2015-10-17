import random

def qsort(A):
    ln =len(A)
    less = []
    equal = []
    greater = []

    if ln > 1:
        pivot = A[0]
        #pivot = A[ln/2]
        #pivot = A[random.randint(0,ln-1)]
        print "pivot", pivot
        for x in A:
            if x < pivot:
                less.append(x)
                print "less --> ", less
            if x == pivot:
                equal.append(x)
                print "equal --> ", equal
            if x > pivot:
                greater.append(x)
                print "greater --> ", greater
        print " "
        return qsort(less)+equal+qsort(greater)
    else:
        return A


a=input("enter array\n")
print "original array", a
print "sorted array : \n", qsort(a)
