import random

def qsort(a):
    if a == []: 
        return []
    else:
        pivot = a[0]
        lesser, equal, greater = partition(a[1:], [], [pivot], [])
        return qsort(lesser) + equal + qsort(greater)

def partition(a, l, e, g):
    while a != []:
        head = a.pop(0)
        if head < e[0]:
            l = [head] + l
        elif head > e[0]:
            g = [head] + g
        else:
            e = [head] + e
    return (l, e, g)


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
            lesser = qsort_alt([x for x in A if x < pivot])
            equal = [x for x in A if x == pivot]
            greater = qsort_alt([ x for x in A if x > pivot])
            """if x < pivot:
                lesser.append(x)
                #print "lesser --> ", less
            if x == pivot:
                equal.append(x)
                #print "equal --> ", equal
            if x > pivot:
                greater.append(x)
                #print "greater --> ", greater"""
        #print " "
        return lesser+equal+greater
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
