
def climb_stair(m):
  if m < 0:
    return 0
  A = [1 for i in range(m)]
  for i in range (1, m):
    if i == 1:
      A[i] = 2
    else:
      A[i] = A[i-2] + A[i-1]
  return A[m-1]

print("Example 1:", climb_stair(3))
print("Example 2:", climb_stair(1))