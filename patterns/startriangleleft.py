n = input("Enter number of rows\n")
temp = n
for i in range(1, n+1):
	for j in range(1, i+1):
		print "*",
	for k in range(1, temp):
		print "x",
	temp = temp-1
	print "\n"
