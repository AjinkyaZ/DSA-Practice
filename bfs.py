from queue import Queue
from graph import Graph, Vertex

def bfs(G, start):
    state = {}
    parentList = {}
    order = []
    #print "bfs started -- start :", start.name
    for vert in G:
        state[vert.name]='undiscovered'
        parentList[vert.name] = None
    state[start.name] = 'discovered'
    Q = Queue()
    Q.enqueue(start)
    while Q.isEmpty() == False:
        u = Q.dequeue()
        order.append(u.name)
        #print "Dequeued vertex", u.name
        #print "vertex adjs "
        #for v in u.connectedTo:
        #    print v.name,
        #print ""
        for v in u.connectedTo:
            if state[v.name] == 'undiscovered':
                state[v.name] == 'discovered'
                parentList[v.name] = u.name
                vert_v = G.getVertex(v.name)
                if Q.contains(vert_v)==False:
                    Q.enqueue(vert_v)
                    #print "Enqueued new", v.name
        state[u.name] = "processed"
    return order
        


def main():
    g = Graph()
    g.addEdge('A', 'B', 'undirected')
    g.addEdge('A', 'E', 'undirected')
    g.addEdge('A', 'F', 'undirected')
    g.addEdge('B', 'C', 'undirected')
    g.addEdge('B', 'E', 'undirected')
    g.addEdge('E', 'D', 'undirected')
    g.addEdge('C', 'D', 'undirected')
    for v in g: print v
    s = g.getVertex('A')
    print "start -->", s.name
    print bfs(g, s)

if __name__ == "__main__":
    main()
