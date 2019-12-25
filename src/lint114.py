from common.utils import printArray;

def unique_path(m, n):
  A = [[1 for i in range(n)] for j in range(m)]
  # printArray(A)
  for i in range(1, m):
    for j in range(1, n):
      A[i][j] = A[i-1][j] + A[i][j-1]

  return A[m-1][n-1]

print("Example 1:", unique_path(1, 3))
print("Example 2:", unique_path(3, 3))
