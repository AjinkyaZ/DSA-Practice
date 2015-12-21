#get avg. percentage of student from list of students, marks --  Hackerrank problem"
n = input("enter number of students \n")
s= []
d = {}
print "enter student name, followed by marks in 3 subjects"
for i in range(n):
    s.append(raw_input())
    s[i] = s[i].split()
for i in range(n):
    d[s[i][0]] = [float(s[i][1]), float(s[i][2]), float(s[i][3])]
print "enter student name whose percentage is required"
x = raw_input()
if x in d:
    n = d[x][0]+d[x][1]+d[x][2]
    res=n/float(3)
    print "average for student ",x,"is {:.2f}".format(res)

else:
    print x, "not in list of students"
