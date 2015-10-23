from stack import Stack

def toexcelnum(str):
	d = len(str)
	S = Stack()
	res = 0
	for i in range(d):
		x = ord(str[i])-64
		S.push(x)
	for i in range(d):
		y = S.pop()
		add = y*(26**i)
		res = res + add
	return res


str = raw_input("enter string\n")
print toexcelnum(str)
