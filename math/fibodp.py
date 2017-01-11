def fibodp(n):
	if f[n] == -1:
		f[n] = fibodp(n-1)+fibodp(n-2)
	return f[n]

def fibodp_driver(n):
	f[0] = 0
	f[1] = 1
	for i in range(2, n):
		f[i] = -1
	return fibodp(n)

x = input("Enter length of seq \n")
f = [-1 for i in range(0,x+1)]
for i in range(0,x):
	print fibodp_driver(i)
