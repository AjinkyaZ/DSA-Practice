##mergesort

def msort(A):
    result = []
    ln = len(A)
    if ln < 2:
        return A
    mid = int(ln/2)
    left = msort(A[:mid])
    right = msort(A[mid:])
    print "left --> ", left
    print "right --> ", right
    print ""
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if left[0] >= right[0]:
                result.append(right[0])
                print "result * ", result
                right.pop(0)
            else:
                result.append(left[0])
                print "result * ", result
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                print "result - ", result
                right.pop(0)
        elif len(left):
            for i in left:
                result.append(i)
                print "result - ", result
                left.pop(0)
    return result

def main():
    #a = [1,7,2,4,6,9,10,23]
    a = raw_input("Enter array\n").split(' ')
    a = [int(i) for i in a]
    print "original array :\n ", a
    print "sorted array :\n", msort(a)


if __name__ == "__main__":
    main()
