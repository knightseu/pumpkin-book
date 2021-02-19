# https://www.techiedelight.com/find-minimum-passes-required-convert-negative-values-matrix/
from collections import deque
mat = [
        [-1, -9, 0, -1, 0],
        [-8, -3, -2, 9, -7],
        [2, 0, 0, -6, 0],
        [0, -7, -3, 5, -4]
    ]
M, N = len(mat), len(mat[0])

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

def isValid(i, j):
    return (0 <= i < M) and (0 <= j < N)

def allPositive():
    for i in range(M):
        for j in range(N):
            if mat[i][j] < 0:
                return False
    return True

def bfs(mat):
    que = deque()
    for i in range(M):
        for j in range(N):
            if mat[i][j] > 0:
                que.append((i, j))

    passes = 0
    while que:
        numLevel =  len(que)
        for i in range(numLevel):
            x, y = que.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if isValid(nx, ny) and mat[nx][ny] < 0:
                    mat[nx][ny] = -1 * mat[nx][ny]
                    que.append((nx, ny))

        passes = passes + 1

    if allPositive():
        print(passes-1)
    else:
        print("Invalid matrix")

if __name__ == '__main__':
    bfs(mat)

