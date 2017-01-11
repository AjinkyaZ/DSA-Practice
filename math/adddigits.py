def digits(a):
    d = 0
    while(a):
        d = d + 1
        a = a/10
    return d

#digital root method
def addDigits(num):
   if num == 0: return 0
   elif num > 9:
       if num%9 == 0:
           return 9
       else:
           return num%9
   else:
       return num

#naive method
def addDigits2(num):
    if num/10 <= 0:
        return num
    n = digits(num)
    sum = 0
    for i in range(n):
        sum = sum + num%10
        num /= 10
    return addDigits(sum)


def main():
    a = input("enter a number\n")
    print "Recursive sum of digits is ", addDigits(a)
    
if __name__ == "__main__":
    main()
