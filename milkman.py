#4 bottles of sizes 1, 5, 7, 10 respectively
b1 = 1
b5 = 5
b7 = 7
b10 = 10
n=input("enter demand\n")
q = 0
div = 0
if n < b5 and n%b1 == 0:
	q1 = n//b1
	div = 1
	if q1>q:
		q = q1  
		print q, "bottles of ", b1, " litres"
if n%b5 == 0:
	q5 = n//b5
	div = 5
	if q5<q:
		q = q5  
		print q, "bottles of ", b5, " litres"
if n%b7 == 0:
	q7 = n//b7
	div = 7
	if q7<q:
		q = q7  
		print q, "bottles of ", b7, " litres"
if n%b10 == 0:
	q10 = n//b10
	div = 10
	if q10<q:
		q = q10 
		print q, "bottles of ", b10, " litres"
if div == 0:
	if n%b10<5:
		q = n%b10
		print q, "bottles of", b1, "litres"
		q = n // b10
		print q, "bottles of", b10, "litres"
	if n%b10<7:
		q = n%b10
		print q, "bottles of", b5, "litres"
		q = n // b10
		print q, "bottles of", b10, "litres"
	if n%b10<10:
		q = n%b10
		print q, "bottles of", b7, "litres"
		q = n // b10
		print q, "bottles of", b10, "litres"