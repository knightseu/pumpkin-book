import sys
from common.tree import TreeNode
from common.tree import in_order_str

# inorder transversal, calculate different, keep track of minimal
def min_bst_diff(root):
  minVal, maxVal, minDiff = inorder(root)
  return minDiff

def inorder(root):
  curMinVal = curMaxVal = root.data
  curMinDiff = sys.maxsize
  if root.left:
    minVal, maxVal, minDiff = inorder(root.left)
    curMinVal = minVal
    curMinDiff = min(curMinDiff, minDiff, root.data - maxVal)
  if root.right:
    minVal, maxVal, minDiff = inorder(root.right)
    curMaxVal = maxVal
    curMinDiff = min(curMinDiff, minDiff, minVal - root.data)
  # print(curMinVal, ",", curMaxVal, ",", curMinDiff)
  return curMinVal, curMaxVal, curMinDiff

a = TreeNode(2)
b = TreeNode(1)
a.left = b
# print(in_order_str(a))
print("Example 1:", min_bst_diff(a))
a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(6)
a.left = b
a.right = c 
d = TreeNode(1)
e = TreeNode(3)
b.left = d 
b.right = e 
# print(in_order_str(a))
print("Example 2:", min_bst_diff(a))