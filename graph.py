class Vertex:
    def __init__(self, key):
        self.name = key
        self.parent = None
        self.successors = {}
        self.connectedTo = {}

    def addNeighbor(self, num, weight=0):
        self.connectedTo[num] = weight

    def __str__(self):
        return str(self.name) + ' connectedTo: ' + str([x.name for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.name

    def getWeight(self, num):
        return self.connectedTo[num]

    def getParent(self):
        return self.parent


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, direction, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        if direction=='undirected':
            self.vertList[t].addNeighbor(self.vertList[f], cost)
        else:
            direction = 'directed'

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def main():
    g = Graph()
    g.addVertex('A')
    g.addVertex('B')
    g.addEdge('A', 'B', 'undirected', 10)
    g.addVertex('C')
    g.addEdge('B', 'C', 15)
    g.addVertex('D')
    g.addEdge('C', 'D', 20)
    for v in g:
        print v

if __name__ == "__main__":
    main()
