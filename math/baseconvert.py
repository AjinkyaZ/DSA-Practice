from stack import Stack

def DectoBin(n):
    bin_no = Stack()
    while n >= 1:
        bin_no.push(n%2)
        n = n // 2
    binString = ""
    while bin_no.isEmpty() == False:
        digit = bin_no.pop()
        binString = binString + str(digit)
    return binString


def BaseConvert(n, base):
    base_num = Stack()
    while n >= 1:
        base_num.push(n%base)
        n = n // base
    baseString = ""
    while base_num.isEmpty() == False:
        digit = base_num.pop()
        baseString = baseString + str(digit)
    return baseString


n = input("Enter decimal number\n")
base = input("Enter base\n")

print BaseConvert(n, base)
