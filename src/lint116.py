def jump_game(A):
  if A is None:
    return False
  if len(A) == 0:
    return False
  
  return True

A = [2,3,1,1,4]
B = [3,2,1,0,4]

print("Example 1:", jump_game(A))
print("Example 2:", jump_game(B))
