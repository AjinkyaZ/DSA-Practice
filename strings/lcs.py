#longest common subsequence
#uses Dynamic Programming

def lcs(X, Y, m, n):
	A = [[0 for i in range(m+2)] for j in range(n+2)]
	for i in range(0, m+1):
		for j in range(0, n+1):
			if i == 0 or j == 0:
				A[i][j] = 0
			elif X[i-1] == Y[j-1]:
				A[i][j] = A[i-1][j-1] + 1
			else:
				A[i][j] = max(A[i-1][j], A[i][j-1])
	return A[m][n]

def max(a, b):
	if a>b:
		return a
	else:
		return b

X = raw_input("Enter string 1\n")
Y = raw_input("Enter string 2\n")
m = len(X)
n = len(Y)
print X, m, "\n", Y, n

print lcs(X, Y, m, n)
