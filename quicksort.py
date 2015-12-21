import random
#in-place quicksort
def qsort(a):
    if len(a) > 1:
        a, pivot = partition(a)
        return qsort(a[:pivot]) + [a[pivot]] + qsort(a[pivot+1:])
    else:
        return a

def partition(a):
    i = 1
    pivot = a[random.randint(0,len(a)-1)]
    for j in range(1,len(a)):
        if a[j] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i-1], a[pivot] = a[pivot], a[i-1]
    return a,i-1

#not in-place
def qsort_alt(A):
    ln =len(A)
    less = []
    equal = []
    greater = []

    if ln > 1:
        #pivot = A[0]
        #pivot = A[ln/2]
        pivot = A[random.randint(0,ln-1)]
        #print "pivot", pivot
        for x in A:
            if x < pivot:
                less.append(x)
                #print "less --> ", less
            if x == pivot:
                equal.append(x)
                #print "equal --> ", equal
            if x > pivot:
                greater.append(x)
                #print "greater --> ", greater
        #print " "
        return qsort_alt(less)+equal+qsort_alt(greater)
    else:
        return A

def main():
    a = raw_input("enter array\n").split(' ')
    a = [int(i) for i in a]
    print "original array :\n", a
    print "sorted array (qsort_alt):\n", qsort_alt(a)
    print ""
    print "sorted array (qsort):\n", qsort(a)

if __name__ == "__main__":
    main()
