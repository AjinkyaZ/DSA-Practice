# Queue Data Structure
# rear of Queue is at index 0


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise KeyError('Queue is empty!')
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def contains(self, item):
        if item in self.items:
            return True
        else:
            return False


def main():
    q = Queue()
    for i in range(1, 4):
        print "enqueued", i
        q.enqueue(i)
    print ""
    print "Queue head at", q.peek()
    print "dequeued", q.dequeue()
    print "dequeued", q.dequeue()
    assert q.size()==1
    print ""
    for i in range(4, 7):
        q.enqueue(i)
        print "enqueued", i
    print ""
    print "Queue head at", q.peek()
    assert q.size()==4
    assert q.contains(4) == True
    while not q.isEmpty():
        x = q.dequeue()
        print "dequeued", x
        assert q.contains(3) == False
        if q.isEmpty() == False:
            print "Queue head at", q.peek()
        else:
            print "Queue empty."

if __name__ == "__main__":
    main()
