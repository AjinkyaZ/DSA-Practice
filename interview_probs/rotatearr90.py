# rotate NxN array by 90 degrees(CW)

def rotatearr90(arr):
	r = len(arr)
	c = len(arr[0])
	arr2 = [[0 for i in range(c)] for j in range(r)]
	for i in range(r):
		for j in range(c):
			arr2[j][c-i-1] = arr[i][j]
	return arr2

def rotate90inplace(arr):
	n=len(arr)
	for i in range(n):
		for j in range(i+1, n):
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
	for i in range(n/2):
		for j in range(n):
			temp = arr[j][n-i-1]
			arr[j][n-i-1], arr[j][i] = arr[j][i], arr[j][n-i-1]
	return arr

#A = input("enter arr\n")
A = [[1,2],[3,4]]
B=[[1,2,3],[4,5,6],[7,8,9]]

print "matrix A :" , A
print "rotated b:", rotatearr90(A)
print "matrix B :", B
print "rotated B:", rotatearr90(B)
print "\n\n\n\n"
print "rotated A:", rotate90inplace(A)
print "rotated B: ", rotate90inplace(B)
