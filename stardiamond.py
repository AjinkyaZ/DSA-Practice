n = input("num of rows\n")
x = raw_input("char 1\n")
y = raw_input("char 2\n")
temp = n/2
for row in range(1,n/2+2):
	for blank in range(1,temp+1):
		print x,
	temp = temp-1
	for star in range(1, 2*row):
		print y,
	print "\n"
temp = 1
for row in range(n/2, 0, -1):
	for blank in range(0, temp):
		print x,
	temp = temp+1
	for star in range(2*row-1, 0, -1):
		print y,
	print "\n"
