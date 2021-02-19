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
  dummyNode = TreeNode("#")
  while curL:
    for i in range(len(curL)):
      # print("Level has ", i, "nodes")
      curNode = curL.pop(0)
      print(curNode.data, end=" ")
      if curNode.left: 
        curL.append(curNode.left)
      elif not curNode == dummyNode:
        curL.append(dummyNode)
      if curNode.right:
        curL.append(curNode.right)
      elif not curNode == dummyNode:
        curL.append(dummyNode)
    print(" ")
      
def buildTree(li):
  # check is i is a valid index of list 'li'
  def isValidIndex(li, i):
    if not li or \
       i < 0 or i >= len(li) or \
       li[i] == '#':
      return False
    return True

  # recursively construct treeNode
  def bT(li, childi, parent):
    if isValidIndex(li, childi):
      parent.left = TreeNode(li[childi])
      bT(li, childi*2+1, parent.left)
    if isValidIndex(li, childi + 1):
      parent.right = TreeNode(li[childi+1])
      bT(li, (childi + 1) * 2 + 1, parent.right)

  if not li or li[0] == '#':
    return
  root = TreeNode(li[0])
  bT(li, 1, root)
  return root



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

  
