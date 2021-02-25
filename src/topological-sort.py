# https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search

class DirectedGraph:
    def __init__(self):
        self.edges = {}
        self.marks = {}

    def addEdge(self, x, y):
        if x in self.edges.keys():
            self.edges[x].append(y)
        else:
            self.edges[x] = y

    def tSort(self):
        for x in self.edges.keys():
            marks[x] = 0

        return
