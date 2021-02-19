# https://www.lintcode.com/problem/486/?_from=ladder&fromId=149
# merge K sorted array
import heapq

mat = [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]

def merge(mat):
    M = len(mat)

    myheap = []
    rst = []

    # a tuple, (value, index of que, position in that que)
    for i in range(M):
        heapq.heappush(myheap, (mat[i][0], i, 0))

    while (len(myheap)):
        val, queIndex, quePos = myheap[0]
        heapq.heappop(myheap)
        rst.append(val)
        if quePos+1 < len(mat[queIndex]):
            heapq.heappush(myheap, (mat[queIndex][quePos+1], queIndex, quePos+1))

    return rst

if __name__ == '__main__':
    print(merge(mat))
