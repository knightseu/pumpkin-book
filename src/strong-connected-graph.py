# https://www.techiedelight.com/check-given-graph-strongly-connected-not/
class Graph:
    def __init__(self, edges, N):
        # assumption is - node starts from 0 to N-1
        self.adjList = [[] for _ in range(N)]
        for (x, y) in edges:
            self.adjList[x].append(y)

def DFS(graph, v, visited):
    visited[v] = True
    for u in graph.adjList[v]:
        if not visited[u]:
            DFS(graph, u, visited)

def strong_connect(graph, N):
    for i in range(N):
        visited = [False] * N
        DFS(graph, i, visited)
        for b in visited:
            if not b:
                return False
    return True

if __name__ == '__main__':
    # List of graph edges as per the above diagram
    edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
 
    # total number of nodes in the graph
    N = 5
 
    # construct graph
    graph = Graph(edges, N)

    if strong_connect(graph, N):
        print("This is a strong connected graph!")
    else:
        print("NOT strong-connected!")

