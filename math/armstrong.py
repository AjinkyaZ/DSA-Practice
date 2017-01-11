def armstrong(N):
    sum_n = 0
    digits = 0
    temp = N
    while temp != 0:
        digits = digits + 1
        temp = temp/10
    temp = N
    while temp != 0:
        rem = temp%10
        sum_n = sum_n + rem**digits
        temp = temp/10

    if N == sum_n:
        print N, " is an armstrong number\n"
        return
    else:
        print N, " is not an armstrong number\n"
        return


n = input("enter number\n")
armstrong(n)


    
