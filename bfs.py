from graph import Graph, Vertex
from queue import Queue


def bfs(g, start):
    state = {}
    for v in g.getVertices():
        state[v] = "undiscovered"
    i = 0
    Q = Queue()
    Q.enqueue(start)
    while Q.isEmpty() == False:
        u = Q.dequeue()
        print u


g = Graph()
g.addVertex('A')
g.addVertex('B')
g.addEdge('A', 'B', 10)
g.addVertex('C')
g.addEdge('B', 'C', 15)
g.addVertex('D')
g.addEdge('C', 'D', 20)

bfs(g, 'A')
