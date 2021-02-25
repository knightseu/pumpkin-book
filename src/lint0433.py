# 0433 number of island
grid1 = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]];
grid2 = [[1, 1]]

# two dimension array, each element is a tuple (x, y)
parent = []

def find(x, y):
    (px, py) = parent[x][y]
    if (x, y) != (px, py):
       parent[x][y] = find(px, py)
    return (x, y)

def union(x1, y1, x2, y2):
    px1, py1 = find(x1, y1)
    px2, py2 = find(x2, y2)

    # optimization: merge small tree to large tree
    if (px1, py1) != (px2, py2):
        parent(px1, py1) = (px2, py2)
