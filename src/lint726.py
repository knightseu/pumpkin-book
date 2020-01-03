from common.tree import TreeNode

def isFullBST(root):
  if not root:
    return True
  
  if not root.left and not root.right:
    return True
  elif root.left and not root.right:
    return False 
  elif not root.left and root.right:
    return False 
  else:
    return isFullBST(root.left) & isFullBST(root.right)

def isFullTree(root):
  # BFS version
  if not root:
    return True
  que = [root]
  while que:
    node = que.pop(0)
    if not node.left and not node.right:
      continue
    elif (not node.left and node.right) or (node.left and not node.right):
      return False
    else:
      que.append(node.left)
      que.append(node.right)
  return True

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b 
a.right = c 
print("Example 1:", isFullBST(a))
print("Example 1:", isFullTree(a))
d = TreeNode(4)
b.left = d
print("Example 2:", isFullBST(a))
print("Example 2:", isFullTree(a))
e = TreeNode(5)
b.right = e
print("Example 3:", isFullBST(a))
print("Example 3:", isFullTree(a))
