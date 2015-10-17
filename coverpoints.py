def makeSpace(X, Y):
    for i in xrange(m):
        print (X[i],Y[i])

    xmax = max(X)
    ymax = max(Y)
    
    print xmax
    print ymax
    AX = [[] for x in range(xmax+1)]
    AY = [[] for y in range(ymax+1)]
    for x in xrange(xmax+1):
        for y in xrange(ymax+1):
            print (x,y)


def coverPoints(X,Y):
    ptList = []
    steps = 0
    for i in xrange(m):
        pt = (X[i], Y[i])
        print pt
        ptList.append(pt)
    print ptList
    lpt = len(ptList)
    print "steps are in incremented total \n"
    for i in xrange(0,lpt-1):
        print "dist between pt", i, " and pt", i+1
        x1 = ptList[i][0]
        y1 = ptList[i][1]
        x2 = ptList[i+1][0]
        y2 = ptList[i+1][1]
        print "point 0: ", (x1,y1)
        print "point 1: ", (x2,y2)
        print "x2-x1 :", (x2-x1)
        print "y2-y1 :", (y2-y1)
        dx = (x2-x1)
        dy = (y2-y1)
        if abs(dx)==abs(dy):
            if dx > 0 and dy > 0:
                steps = steps + abs(dx)
                print "to bottom right"
                print steps
            if dx < 0 and dy > 0:
                steps = steps + abs(dx)
                print "to bottom left"
                print steps
            if dx < 0 and dy < 0:
                steps = steps + abs(dx)
                print "to top left"
                print steps
            if dx > 0 and dy < 0:
                steps = steps + abs(dx)
                print "to top right"
                print steps
        else:
            if x2>x1:
                steps = steps + abs(dx)
                print "to right"
                print steps
            if x2<x1:
                steps = steps + abs(dx)
                print "to left"
                print steps
            if y2>y1:
                steps = steps + abs(dy)
                print "to bottom"
                print steps
            if y2<y1:
                steps = steps + abs(dy)
                print "to top"
                print steps

        
m =  input("num of points\n")
X = [[] for x in range(0,m)]
print X
Y = [[] for x in range(0,m)]
print Y
for i in xrange(m):
    print "point :", i
    X[i] = input("xcoord : ")
    Y[i] = input("ycoord : ")
    print ""

coverPoints(X,Y)

