import numpy
from common.tree import TreeNode
from common.tree import printByLevel

def get_pow2_range(x: int):
    if x<=1:
        return 1;
    rst = 1
    rbound = 2
    while x>rbound:
        rst += 1
        rbound *= 2
    return rst



def build_tree(nodes: []):
    def buildTreenode(val):
        if val == '#':
            return None
        else:
            return TreeNode(val)
    print(nodes)
    tree_levels = get_pow2_range(len(nodes))
    print("Buiding tree with levels: ", tree_levels)
    root = None
    index = 0
    prev_level = []
    for i in range(tree_levels):
        
        if i == 0:
            node = TreeNode(nodes[0])
            prev_level.append(node)
            root = node
            index = 1
            continue
        
        num = pow(2, i-1)

        cur_level = []
        for j in range(num):
            if index >= len(nodes) - 1 :
                break
            nodel = buildTreenode(nodes[index])
            noder = buildTreenode(nodes[index+1])
            prev_level[j].left = nodel
            prev_level[j].right = noder
            cur_level.append(nodel)
            cur_level.append(noder)
            index += 2
        prev_level = cur_level

    return root


def build_tree2(nodes: []):
    def buildTreenode(val):
        if val == '#':
            return None
        else:
            return TreeNode(val)   
    # for node in nodes:
    index = -1
    level = 1
    prev = []
    cur = []
    while index < len(nodes):
        if len(cur) == 0:
        for i in range(pow(2, level-1)):
            ### pow(2, level-1) => 1, 2, 4, 8 .....
            index += 1
            node = buildTreenode(nodes[index])

    pass

printByLevel(build_tree([6, 2, 8, 0, 4, 7, 9, '#', '#', 3, 5]))