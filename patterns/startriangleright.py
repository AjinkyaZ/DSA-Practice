n = input("Enter num of rows\n")
temp = n
for i in range(1, n+1):
	for j in range(1, temp):
		print "X",
	temp =  temp - 1
	for k in range(1, i+1):
		print "*",
	print "\n"  
