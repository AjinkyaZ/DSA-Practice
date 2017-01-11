def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:	
		return fibo(n-1)+fibo(n-2)
x = input("Enter length of seq \n")
for i in range(x):
	print fibo(i)
