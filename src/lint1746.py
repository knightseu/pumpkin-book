from common.tree import TreeNode
from common.tree import in_order_str

def min_bst_diff(root):
  return 0

a = TreeNode(2)
b = TreeNode(1)
a.left = b
print(in_order_str(a))
print("Example 1:", min_bst_diff(a))