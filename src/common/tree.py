class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.data = val
  
def in_order_str(root):
  if root is None:
    return ""
  else:
    return in_order_str(root.left) + str(root.data) + in_order_str(root.right)


  