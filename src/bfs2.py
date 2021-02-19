from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.visited[u] = False

    def BFS(self, src):
        que = []
        que.append(src)
        self.visited[src] = True

        while que:
            s = que.pop(0)
            print(s, end = " ")
            print("========")
            for t in self.graph[s]:
                if self.visited[t] == False:
                    que.append(t)
                    self.visited[t] = True



    def print(self):
        from pprint import pprint
        pprint(self.graph)

g =  Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
