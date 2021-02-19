# https://www.lintcode.com/problem/486/?_from=ladder&fromId=149
# merge K sorted array
mat = [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]

def merge(mat):
    M = len(mat)

    myheap = []
    rst = []
    import pdb; pdb.set_trace()

    for i in range(M):
        heappush(myheap, mat[i][0])

    rst.append(heappop(myheap))

    return rst

if __name__ == '__main__':
    print(merge(mat))
