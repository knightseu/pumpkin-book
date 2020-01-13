import math

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

def printByLevel(root):
  if not root:
    return None
  curL = [root]
  while curL:
    for i in range(len(curL)):
      # print("Level has ", i, "nodes")
      curNode = curL.pop(0)
      print(curNode.data, end=" ")
      if curNode.left:
        curL.append(curNode.left)
      if curNode.right:
        curL.append(curNode.right)
    print(" ")
      

def genCompleteBinaryTree(level):
  if level <= 0:
    return None
  
  prevLevelNodes = []
  curVal = 0
  root = None
  for i in range(level):
    curNodes = []
    for j in range(int(math.pow(2, i))):
      curVal += 1
      # print(curVal, end = " ")
      curNodes.append(TreeNode(curVal))
    if (prevLevelNodes):
      for i in range(len(prevLevelNodes)):
        prevLevelNodes[i].left = curNodes[2 * i]
        prevLevelNodes[i].right = curNodes[2 * i + 1]
    else:
      root = curNodes[0]
    prevLevelNodes = curNodes
  
  # printByLevel(root)
  return root

  