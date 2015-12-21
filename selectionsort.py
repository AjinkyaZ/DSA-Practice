def selection_sort(A):
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
	        min = j
	A[i], A[min] = A[min], A[i]
    return A


def main():
    a = raw_input("enter array\n").split(' ')
    a = [int(n) for n in a]
    print "original array : \n", a
    print "sorted array : \n", selection_sort(a)

if __name__ == "__main__":
    main()

