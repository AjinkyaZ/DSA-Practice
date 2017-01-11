from stack import Stack


class StackedQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.isEmpty():
            raise KeyError('Queue is empty!')
        if self.s2.size() > 0:
            return self.s2.pop()
        while self.s1.size() > 1:
            d = self.s1.pop()
            self.s2.push(d)
        if self.s1.size() == 1:
            return self.s1.pop()
        else:
            return self.s2.pop()

    def peek(self):
        if self.isEmpty():
            raise KeyError('Queue is empty!')
        if self.s2.size() > 0:
            return self.s2.items[-1]
        else:
            return self.s1.items[0]

    def size(self):
        sq_size = self.s1.size() + self.s2.size()
        return sq_size

    def contains(self, item):
        if item in self.s1.items or item in self.s2.items:
            return True
        else:
            return False


def main():
    sq = StackedQueue()
    for i in range(1, 4):
        print "enqueued", i
        sq.enqueue(i)
    print ""
    print "Queue head at", sq.peek()
    print "dequeued", sq.dequeue()
    print "dequeued", sq.dequeue()
    assert sq.size()==1
    print ""
    for i in range(4, 7):
        sq.enqueue(i)
        print "enqueued", i
    print ""
    print "Queue head at", sq.peek()
    assert sq.size()==4
    assert sq.contains(4) == True
    while not sq.isEmpty():
        x = sq.dequeue()
        print "dequeued", x
        assert sq.contains(3) == False
        if sq.isEmpty() == False:
            print "Queue head at", sq.peek()
        else:
            print "Queue empty."

if __name__ == "__main__":
    main()
