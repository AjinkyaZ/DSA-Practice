# given array of size n, nums from 1 to n in any order with one number
# missing and one number repeated, return missing and repeated number


def repeatedNumber(A):
    la = len(A)
    sumact = 0
    sumarr = 0
    sumactsqr = 0
    sumarrsqr = 0
    for i in range(1, la + 1):
        sumact = sumact + i
        sumactsqr = sumactsqr + i**2
    # print "sumact, sumactsqr \n", sumact, sumactsqr
    for i in A:
        sumarr = sumarr + i
        sumarrsqr = sumarrsqr + i**2
    # print "sumarr , sumarrsqr\n", sumarr, sumarrsqr
    # repeat-missing
    x = sumact - sumarr
    #repeat^2 - missing^2
    y = sumactsqr - sumarrsqr
    # now r^2 - m^2 = (r+m)*(r-m)
    # therefore r+m = y//x
    c = y // x  # r+m
    m = (c + x) // 2
    r = m - x
    return m, r


print repeatedNumber([1, 3, 5, 2, 3])
