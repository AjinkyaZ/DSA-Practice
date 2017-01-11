import random

# 10 days - 0 to 9
L = [x for x in xrange(10)]
H = [x for x in xrange(10)]
S = [x for x in xrange(10)]
P = [x for x in xrange(10)]
for i in xrange(10):
    L[i]= format(random.uniform(3.0, 4.7), '.2f')
    S[i] = format(random.uniform(3.5, 4.8), '.2f')
    while(True):
        H[i] = format(random.uniform(3.9, 5.6), '.2f')
        if H[i] > L[i] :
            break

print "Starting", S
print "Lows", L
print "Highs", H
#L = input("daily Lows\n")
#H = input("daily highs\n")
#S = input("daily Starting price\n")

d = float(S[0]) - float(S[1])
print float(S[0])
print float(S[1])
print "diff 1st", d

for j in xrange(10):
    for i in xrange(j):
        P[i] = format((float(S[j]) - float(S[i])), '.2f')
        if P[i] > d:
            d = P[i]
            print "new d", d

print P
        
