import graph
import heapq


def build_gallon_graph(g, jug1, jug2, jug1_size, jug2_size):
    """Build a graph for solving a jug problem. Recursive function.

    Arguments:
        g -- graph.Graph() object.
        jug1 -- Amount of water in a first jug.
        jug2 -- Amount of water in a second jug.
        jug1_size -- Size of the first jug.
        jug2_size -- Size of the second jug.
    """
    # Fill jug 1.
    if jug1 < jug1_size:
        new_jug1, new_jug2 = jug1_size, jug2
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)

    # Fill jug 2.
    if jug2 < jug2_size:
        new_jug1, new_jug2 = jug1, jug2_size
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)

    # Pour jug 1 to jug 2.
    if jug1 > 0 and jug2 < jug2_size:
        new_jug1 = jug1 - jug2_size + jug2
        if new_jug1 < 0:
            new_jug1 = 0
        new_jug2 = jug2 + jug1 if jug1 + jug2 <= jug2_size else jug2_size
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)

    # Pour jug 2 to jug 1.
    if jug2 > 0 and jug1 < jug1_size:
        new_jug1 = jug2 + jug1 if jug1 + jug2 <= jug1_size else jug1_size
        new_jug2 = jug2 - jug1_size + jug1
        if new_jug2 < 0:
            new_jug2 = 0
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)

    # Empty jug 1.
    if jug1 > 0:
        new_jug1, new_jug2 = 0, jug2
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)

    # Empty jug 2.
    if jug2 > 0:
        new_jug1, new_jug2 = jug1, 0
        _add_connection(g, jug1, jug2, new_jug1, new_jug2,
                        jug1_size, jug2_size)


def _connection_exists(g, jug1, jug2, new_jug1, new_jug2):
    if (new_jug1, new_jug2) not in g.vertices or (jug1, jug2) not in g.vertices:
        return False
    if g.vertices[(new_jug1, new_jug2)] in g.vertices[(jug1, jug2)].neighbors:
        return True
    if g.vertices[(jug1, jug2)] in g.vertices[(new_jug1, new_jug2)].neighbors:
        return True
    return False


def _add_connection(
        g, jug1, jug2, new_jug1, new_jug2, jug1_size, jug2_size):
    if not _connection_exists(g, jug1, jug2, new_jug1, new_jug2):
        g.add_edge((jug1, jug2), (new_jug1, new_jug2))
        build_gallon_graph(g, new_jug1, new_jug2, jug1_size, jug2_size)


def find_correct_order_of_actions(g, start, finish):
    """This is based on Dijkstra's shortest path alogirthm."""
    g.vertices[start].distance = 0
    queue = [(v.distance, v) for v in g.vertices.values()]
    heapq.heapify(queue)
    while queue:
        _, vertex = heapq.heappop(queue)
        for neighbor in vertex.neighbors:
            distance = vertex.distance + vertex.neighbors[neighbor]
            if distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.predecessor = vertex
                heapq._siftdown(queue, neighbor, distance)
    path = []
    vertex = g.vertices[finish]
    while vertex.predecessor is not None:
        path.append(vertex)
        vertex = vertex.predecessor
    path.append(vertex)
    return reversed(path)

jug1, jug2 = 0, 0
jug1_size, jug2_size = 4, 3
jug2_result, jug1_result = 2, 0

g = graph.Graph()
g.add_vertex((jug1, jug2))
build_gallon_graph(g, jug1, jug2, jug1_size, jug2_size)
path = find_correct_order_of_actions(
        g, (jug1, jug2), (jug1_result, jug2_result))
for vertex in path:
    print '({}-gallon jug: {}, {}-gallon jug: {})'.format(
            jug1_size, vertex.key[0], jug2_size, vertex.key[1])

