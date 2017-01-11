#reverse a string
#python strings are immutable, so used list
s = raw_input("enter string\n")
li = list(s)
n = len(li)
for i in range(n/2):
    temp = li[i]
    li[i] = li[n-i-1]
    li[n-i-1] = temp
s = ''.join(li)
print s
