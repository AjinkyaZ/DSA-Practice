#integer array/list
def insertion_sort(arr):
	n = len(arr)
	A = []
	for i in arr:
		A.append(i)
	for i in range(1,n):
		j=i
		while j>0 and A[j] < A[j-1]:
			temp = A[j]
			A[j] = A[j-1]
			A[j-1] = temp
			j -= 1
	return A

def main():
    arr = raw_input("enter array elements\n")
    arr = arr.split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    print "original array : \n", arr
    print "sorted array :\n", insertion_sort(arr)
    #st1 = raw_input("enter string\n")
    #print insertion_sort(st1)

if __name__ == "__main__":
	main()
