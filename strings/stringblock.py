#find start index of largest block of repeating chars in a string

def stringblock(string):
	ls = len(string)
	res = []
	if ls == 1:
		res = [1,string[0],0]
		return res
	index = -1
	len_block = 1
	check_lb = 1
	char = None
	for i in range(ls-1):
		#print "char :", string[i],
		if string[i] == string[i+1]:
			len_block += 1
			if len_block>check_lb:
				check_lb=len_block
				index = i-check_lb+2
		else:
			if check_lb < len_block:
				check_lb = len_block
			len_block=1
		#print ",cb:", check_lb, ", lenblock:", len_block
	res = [check_lb, string[index], index]
	return res

s = raw_input("enter string\n")
ans = stringblock(s)
print "length of largest block:", ans[0], ", char:", ans[1]," index:", ans[2]

