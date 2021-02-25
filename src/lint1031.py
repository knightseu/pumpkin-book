# biparity https://www.jiuzhang.com/problem/is-graph-bipartite/
from collections import deque

class Graph:
    def __init__(self):
        self.edges = {}
        self.visited = {}
    def addEdge(self, x, y):
        if x in self.edges.keys():
            self.edges[x].append(y)
        else:
            self.edges[x] = [y]
        if y in self.edges.keys():
            self.edges[y].append(x)
        else:
            self.edges[y] = [x]

    def init(self, edges):
        for (x, y) in edges:
            self.addEdge(x, y)

    def bfs(self, src):
        que = deque()
        que.append(src)
        self.visited = {}
        for node in self.edges.keys():
            self.visited[node] = 0

        group = 1
        while que:
            M = len(que)
            for i in range(M):
                cur = que.popleft()

                self.visited[cur] = group
                for dest in self.edges[cur]:
                    if self.visited[dest] == 0:
                        que.append(dest)

            if group == 1:
                group = 2
            else:
                group =1

        # check biparite

edges = [(0,3), (0,1), (1,2), (3, 2)]
g = Graph()
g.init(edges)

# print(len(g.edges))
g.bfs(0)
