
# 1.Greedy version
def jump_game_greedy(A):
  if A is None:
    return False
  if len(A) == 0:
    return False
  i = 0
  while i < len(A) -1:
    if (A[i] == 0):
      return False
    i += A[i]

  if i < len(A) - 1:  
    return False
  
  return True

# 2.Dynamic Programming
def jump_game(A):
  if A is None:
    return False
  if len(A) == 0:
    return False
  
  m = len(A)
  canJump = [False for i in range(m)]
  canJump[0] = True # we start from here
  for i in range(1, m):
    for j in range(i):
      if canJump[j] & (j + A[j] >= i):
        canJump[i] = True
        break
  
  # print(*canJump, sep=",")
  return canJump[m-1]

A = [2,3,1,1,4]
B = [3,2,1,0,4]

print("Example 1:", jump_game(A))
print("Example 2:", jump_game(B))
