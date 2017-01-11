n = input("Enter number of rows\n")

for i in range(n+1, 1, -1):
	for j in range(1, i):
		print j,
	print "\n"

