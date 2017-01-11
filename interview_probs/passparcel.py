from queue import Queue


def passparcel(names, n):
    pass_queue = Queue()
    for name in names:
        pass_queue.enqueue(name)

    while pass_queue.size() > 1:
        for i in range(n):
            pass_queue.enqueue(pass_queue.dequeue())
            
        pass_queue.dequeue()

    return pass_queue.dequeue()



names = input("Enter List of Names \n")
n = len(names)
print passparcel(names, n)
