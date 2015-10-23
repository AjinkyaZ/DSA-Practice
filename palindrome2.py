def isPalindrome(A):
        div = 1
        while int(A//div) >= 10:
            div = div*10
        while A != 0:
            left = int(A//div)
            right = A % 10
            if left != right:
                return False
            A = (A % div)//10
            div = div//100
        return True

n = input("num\n")
print isPalindrome(n)
