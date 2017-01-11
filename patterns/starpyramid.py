n = input("Enter number of rows\n")
temp = n
for i in range(1, n+1):
	for j in range(1, temp):
	#print x instead of spaces, helps to visualize loop
		print "x",
	temp = temp - 1
	for k in range(1, (2*i)):
		print "*",
	print "\n" 
