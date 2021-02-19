# https://www.lintcode.com/problem/1311?_from=ladder&fromId=29

from common.tree import TreeNode, buildTree, printByLevel

def lca(root, v1, v2):
    if root is None or \
       root.data == v1 or root.data == v2:
        return root

    left_lca = lca(root.left, v1, v2)
    right_lca = lca(root.right, v1, v2)

    if left_lca and right_lca:
        return root

    return left_lca if right_lca is None else left_lca


l1 = [6,2,8,0,4,7,9,'#','#',3,5]

root = buildTree(l1)
printByLevel(root)

printByLevel(lca(root, 3, 5))
