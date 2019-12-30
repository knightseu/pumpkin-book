from common.tree import TreeNode
from common.tree import in_order_str

def trimTree(root, lBound, rBound):
  if not root:
    return None
  if (root.data < lBound): 
    return trimTree(root.right, lBound, rBound)
  elif (root.data > rBound):
    return trimTree(root.left, lBound, rBound)
  else:
    root.left = trimTree(root.left, lBound, rBound)
    root.right = trimTree(root.right, lBound,rBound)
  return root

print("701")
a = TreeNode(8)

b = TreeNode(3)
c = TreeNode(10)
a.left = b 
a.right = c 
d = TreeNode(1)
e = TreeNode(6)
b.left = d 
b.right = e 
f = TreeNode(4)
g = TreeNode(7)
e.left = f
e.right = g 
h = TreeNode(14)
c.right = h
k = TreeNode(13)
h.left = k
print(in_order_str(a))
root = trimTree(a, 5, 13)
print(in_order_str(root))

