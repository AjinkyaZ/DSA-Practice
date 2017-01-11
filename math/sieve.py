from datetime import datetime
from math import sqrt

def sieve_a(n):
        primes = []
        for i in xrange(0,n+1):
            primes.append(1)
        primes[0] = 0
        primes[1] = 0
        for i in xrange(2, (n+1)):
            #print i
            if primes[i] == 1:
                j=2
                while (i*j) <= n:
                    primes[i*j] = 0
                    j = j+ 1
        prime_list = []
        for i in xrange(0, (n+1)):
            if primes[i] == 1:
                prime_list.append(i)
        return prime_list

def sieve_b(n):
        primes = []
        for i in xrange(0,n+1):
            primes.append(1)
        primes[0] = 0
        primes[1] = 0
        m =  int(sqrt(n))
        for i in xrange(2, (m+1)):
            #print i
            if primes[i] == 1:
                j=2
                while (i*j) <= n:
                    primes[i*j] = 0
                    j = j+ 1
        prime_list = []
        for i in xrange(0, (n+1)):
            if primes[i] == 1:
                prime_list.append(i)
        return prime_list
    
x = input("no \n")
start = datetime.now()
print sieve_a(x)
print (datetime.now() - start)
start2  = datetime.now()
print sieve_b(x)
print (datetime.now() - start2)
