from deque import Deque


def palindromeCheck(string):
    char_deque = Deque()

    for char in string:
        char_deque.addRear(char)
    pal = True

    while char_deque.size() > 1 and pal == True:
        head = char_deque.removeFront()
        tail = char_deque.removeRear()
        if head != tail:
            pal = False

    return pal

str_a = raw_input("Enter word/string \n")
print palindromeCheck(str_a)
