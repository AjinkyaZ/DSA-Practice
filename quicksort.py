import random


def qsort(a):
    qsort_args(a, 0, len(a) - 1)


def qsort_args(a, start, end):
    if start < end:
        pivot = partition(a, start, end)
        qsort_args(a, start, pivot - 1)
        qsort_args(a, pivot + 1, end)


def partition(a, start, end):
    pivot = start + random.randrange(end - start + 1)
    a[pivot], a[end] = a[end], a[pivot]
    for i in range(start, end):
        if a[i] <= a[end]:
            a[i], a[start] = a[start], a[i]
            start += 1
    a[start], a[end] = a[end], a[start]
    return start


def qsort_alt(A):
    ln = len(A)
    less = []
    equal = []
    greater = []

    if ln > 1:
            #pivot = A[0]
            #pivot = A[ln/2]
        pivot = A[random.randint(0, ln-1)]
        # print "pivot", pivot
        for x in A:
            lesser = qsort_alt([x for x in A if x < pivot])
            equal = [x for x in A if x == pivot]
            greater = qsort_alt([x for x in A if x > pivot])
            """if x < pivot:
                lesser.append(x)
                #print "lesser --> ", less
            if x == pivot:
                equal.append(x)
                #print "equal --> ", equal
            if x > pivot:
                greater.append(x)
                #print "greater --> ", greater"""
        # print " "
        return lesser+equal+greater
    else:
        return A


def main():
    arr = raw_input("enter array\n").split(' ')
    arr = [int(i) for i in arr]
    print "original array :\n", arr
    print "sorted array (qsort_alt):\n", qsort_alt(arr)
    print ""
    qsort(arr)
    print "sorted array (qsort):\n", arr

if __name__ == "__main__":
    main()
