#count occurence of num in array - uses variant of binary search
def findIndex(A, k, index):
	if k not in A:
	    return 0
	lo = 0
	hi = len(A)-1
	res = -1
	while lo <= hi:
		mid = lo + (hi-lo)/2
		if A[mid] == k:
			res = mid
			if index == "first":
				hi = mid-1
			elif index == "last":
				lo = mid+1
		elif A[mid] < k:
			lo = mid+1
		else:
			hi = mid-1
	return res


def findCount(A, k):
    n = len(A)
    count = 0
    for i in range(n):
        if A[i] == k:
            count += 1
        elif A[i] > k:
            break
    return count

arr = input("Enter sorted array of nums\n")
print arr
key = input("Enter num in array\n")
occurence = (findIndex(arr, key, "last") - findIndex(arr, key, "first"))+1
print key, "occurs ", occurence, "times in given array"
