import numpy as np
from adjacency_matrix import AdjacencyMatrixGraph

def depth_first(graph, visited, current=0):
    if visited[current] == True:
        return

    visited[current] = True
    print(f'Visit: {current}')

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


if __name__ == '__main__':
    g: AdjacencyMatrixGraph = AdjacencyMatrixGraph(9)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2 ,7)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 4)
    g.add_edge(6, 8)

    visited: np.ndarray = np.zeros(g.numVertices)
    depth_first(g, visited)
