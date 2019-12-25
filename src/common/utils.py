def printArray(A):
  m = len(A)
  n = len(A[0])
  for i in range(m):
    for j in range(n):
      print(A[i][j], end = ",")
    print(" ")
