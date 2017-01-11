#program to check if parantheses are balanced

from stack import Stack

def ParaChecker():
    s = Stack()
    bal = True
    i = 0
    for i in xrange(len(string)):
        p = string[i]
        if p == '(':
            s.push(p)
        else:
            if s.isEmpty():
                bal = False
            else:
                s.pop()

    if bal and s.isEmpty():
        return True
    else:
        return False


string = raw_input("enter parastring\n")
print ParaChecker(string)    
        
