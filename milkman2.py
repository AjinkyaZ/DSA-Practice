def left(d, L):

	if d==0:
		l =0
	elif d == 1:
		l=1
	elif d == 2:
		l=2
	elif d == 3:
		l=3
	elif d == 4:
		l=4
	elif d == 5:
		l=1
	elif d == 6:
		l=2
	elif d == 7:
		l=1
	elif d == 8:
		l=2
	elif d == 9:
		l=3
	L = L+l
	return L

def min(a, b):
	if a<b:
		return a
	else:
		return b

Demand= input("enter\n")
#n,Demand,litres,L,L10,L7,L5
lit = Demand // 10
L = lit
lit = lit * 10
Demand = Demand - lit
L10 = left(Demand, L)

lit = Demand // 7
L = lit
lit = lit * 7
Demand = Demand - lit
L7 = left(Demand, L)

lit = Demand // 5
L = lit
lit = lit * 5
Demand = Demand - lit
L5 = left(Demand, L)

print min(L5, min(L10, L7))