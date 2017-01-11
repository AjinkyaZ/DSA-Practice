def setZeroes(A):
        rowFlag = False
        colFlag = False
        m = len(A)
        if m == 0:
            return A
        n = len(A[0])
        if n == 0:
            return A
        for i in range(n):
            if A[0][i] == 0:
                rowFlag = True
                break
        for i in range(m):
            if A[i][0] == 0:
                colFlag = True
                break
        for i in range(1,m):
            for j in range(1,n):
                if A[i][j] == 0:
                    A[0][j] = 0
                    A[i][0] = 0
        
        for i in range(1,m):
            for j in range(1,n):
                if A[0][j] == 0 or A[i][0] == 0:
                    A[i][j] = 0
        if rowFlag:
            for i in range(n):
                A[0][i] = 0
        if colFlag:
            for i in range(m):
                A[i][0] = 0
        return A

#A = [[0,1,1],[1,1,1],[1,1,0]]
r = int(raw_input("Enter number of rows for array: \n"))
c = int(raw_input("Enter number of columns for array: \n"))
A = []
print "Enter array elements :"
for i in range(r):
    print "enter row elements separated by spaces: row", i
    d = [int(i) for i in raw_input().split()]
    assert len(d) == c
    A.append(d)
print "Original Array :"
for i in A:
    print i
print "Modified Array :"
A_zero = setZeroes(A)
for i in A_zero:
    print i
