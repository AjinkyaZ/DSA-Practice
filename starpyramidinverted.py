n = input("Enter number of rows\n")

temp = 1
for row in range(n, 0, -1):
    #print zeros instead of blanks for visualizing loop
    for k in range(0, temp-1):
	print "0",
    temp = temp+1
    for i in range(2*row-1, 0, -1):
	print "*",
    print "\n"
 
