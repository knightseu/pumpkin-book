from common.tree import TreeNode

mp = {}
def partitionEqualTree(root):
  sum = transversal(root)
  return sum%2 == 0 and sum/2 in mp

def transversal(root):
  if root == None:
    return 0
  sum = root.data + transversal(root.left) + transversal(root.right) 
  if not sum in mp:
    mp[sum] = 1
  return sum
