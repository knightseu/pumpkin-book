# https://www.techiedelight.com/count-the-number-of-islands/
from collections import deque

# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 1, 0, -1, -1, 1, 0, 1]

def isValid(mat, x, y, visited):
    return (x >= 0) and (x < len(visited)) and \
        (y >= 0) and (y < len(visited[0])) and \
        mat[x][y] == 1 and \
        not visited[x][y]

def BFS(mat, x, y, visited):
    que = deque()
    que.append((x, y))

    visited[x][y] = True

    while que:
        cx, cy = que.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if isValid(mat, nx, ny, visited):
                visited[nx][ny] = True
                que.append((nx, ny))

if __name__ == '__main__':
 
    mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]
 
    (M, N) = (len(mat), len(mat[0]))

    visited = [[False for x in range(M)] for y in range(N)]

    print(M, N)

    island = 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1 and not visited[i][j]:
                BFS(mat, i, j, visited)
                island = island + 1

    print(island)
