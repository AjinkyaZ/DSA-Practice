def binarySearch(A, key):
   lo = 1
   hi = len(A)
   while lo <= hi:
      mid = lo + (hi-lo)/2
      if A[mid] == key:
         return mid
      elif A[mid] < key: 
         lo = mid+1
      else:
         hi = mid-1

    
A = input("enter array\n")
A = sorted(A)
print "sorted Array --> ", A
k = input("enter key\n")
if k not in A:
    print "invalid key: not in array"
    quit()
res = binarySearch(A, k)
if res == None: res = 0
print "key found at index ", res
