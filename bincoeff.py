def bin_coeff(n, m):
	bc = [[-1 for i in range(MAXN)] for j in range(MAXN)]
	for i in range(n+1):
		bc[i][0] = 1
	for j in range(n+1):
		bc[j][j] = 1
	for i in range(1, n+1):
		for j in range(1, i):
			bc[i][j]=bc[i-1][j-1]+bc[i-1][j]
	return bc[n][m]


MAXN = 100
n = input("enter order of equation \n")
for x in range(n+1):
	print "order", x, ":",
	for y in range(x+1):
		#print "[", x, ",", y, "] : ", bin_coeff(x, y)
		print bin_coeff(x, y),
	print "\n"
