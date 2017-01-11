# solution for a hackerrank problem -- get abs value of difference of sum of elements along both diagonals of array (diag2 - diag1)
def diagDiff(arr):
	i = 0
	j = 0
	sumd1 = 0
	sumd2 = 0
	while i < n and j < n:
		sumd1 = sumd1 + arr[i][j]
		i +=1
		j +=1
	i = n-1
	j=0
	while i >= 0 and j < n:
		sumd2 = sumd2 + arr[i][j]
		i -=1
		j +=1
	return abs(sumd2-sumd1)


n = input()
arr = [[0 for i in range(n)] for j in range(n)]
print arr
for i in range(n):
	arr[i] = raw_input().split()
	for j in range(n):
		arr[i][j] = int(arr[i][j])
print arr
print diagSum(arr)
