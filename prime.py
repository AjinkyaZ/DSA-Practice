from math import sqrt
def is_prime(n):
    upperlim =  int(sqrt(n))
    if n == 1: return "is not a prime"
    for i in xrange(2, upperlim + 1):
        if i > 1 and n % i == 0:
            return "is not a prime"
    return "is a prime"
#n = input("enter number\n")
#print n, is_prime(n)
