from common.tree import TreeNode
from common.tree import genCompleteBinaryTree
from common.tree import printByLevel

def dfsTree(root):
  while root:
    print(root.data)
    dfsTree(root.left)
    dfsTree(root.right)


node1 = genCompleteBinaryTree(4)
printByLevel(node1)

