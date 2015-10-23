# Queue Data Structure
# rear of Queue is at index 0


class Queue():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def contains(self, item):
        if item in self.items:
            return True
        else:
            return False
