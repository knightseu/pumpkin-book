# https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
# https://www.geeksforgeeks.org/topological-sorting/

class DirectedGraph:
    def __init__(self):
        self.edges = {}
        self.marks = {}
        self.tsort = []

    def addEdge(self, x, y):
        if x in self.edges.keys():
            self.edges[x].append(y)
        else:
            self.edges[x] = [y]

        if not x in self.marks.keys():
            self.marks[x] = 0
        if not y in self.marks.keys():
            self.marks[y] = 0


    def dfs(self, v):
        # import pdb; pdb.set_trace()
        if self.marks[v] == 2:
            return

        if self.marks[v] == 1:
            print("---cycle!!!")
            return

        self.marks[v] = 1
        if v in self.edges.keys():
            for node in self.edges[v]:
                self.dfs(node)
        self.marks[v] = 2
        self.tsort.append(v)

    def tSort(self):
        # reset marks
        for x in self.marks.keys():
            self.marks[x] = 0

        # for unmarked node, do dfs
        for x in self.edges.keys():
            if self.marks[x] == 0:
                self.dfs(x)
        return

if __name__ == '__main__':
    g = DirectedGraph()
    g.addEdge(5, 0)
    g.addEdge(5, 2)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.tSort()
    print(g.tsort)
