def getLamps(a):
    flag = 0
    for i in xrange(len(a)):
        if a[i] == 'F':
            #flag unchanged
            continue
        else:
            flag = 1
            return i+1
    if flag == 0:
            return flag



a = raw_input("enter sequence \n")
a = a.upper()
print a
for x in a:
    if x != 'F' and x!= 'T':
        print "enter valid values"
        quit()

print getLamps(a)
