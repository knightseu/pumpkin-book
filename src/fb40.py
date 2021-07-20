# fb top 40 -educative
# https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions#questions

from common.tree import TreeNode
from common.tree import printByLevel
import pickle
import sys

#1. Move 0 to the left
def move_array_0_left(arr):
    if len(arr) < 1:
        return
    r_idx = len(arr) - 1
    w_idx = len(arr) - 1

    while r_idx >= 0:
        if not arr[r_idx] == 0:
            arr[w_idx] = arr[r_idx]
            w_idx = w_idx - 1
        r_idx = r_idx - 1
    while w_idx > r_idx:
        arr[w_idx] = 0
        w_idx = w_idx - 1

    print(arr)


#2. Merge overlapping intervals
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def merge_intervals(arr):
    rst = []
    if not arr:
        return rst

    rst.append(arr[0])

    if len(arr) == 1:
        return rst

    for i in range(1, len(arr)):
        x1 = arr[i].first
        y1 = arr[i].second
        x2 = rst[-1].first
        y2 = rst[-1].second

        if y2 < x1:
            rst.append(Pair(x1, y1))
        else:
            rst[-1].second = max(y1, y2)

    return rst


#3. Convert binary tree to doubly linked list
def connect_dblist(h1, h2):
    if h1 == None:
        return h2
    if h2 == None:
        return h1

def convert_binary_tree(root):
    if root:
        head = None
        tail = None
        l_head, l_tail = convert_binary_tree(root.left)
        r_head, r_tail = convert_binary_tree(root.right)
        root.left = l_tail
        if l_tail:
            l_tail.right = root
            head = l_head
        else:
            head = root
        root.right = r_head
        if r_head:
            r_head.left = root
            tail = r_tail
        else:
            tail = root
        return head, tail
    return None, None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = ",")
        inorder(root.right)

#4. Level order traversal of binary tree
def level_traversal(root):
    if not root:
        return

    from collections import deque

    q = deque()
    q.append(root)

    while (len(q) > 0):
        for i in range(len(q)):
            node = q.popleft()
            print(node.data, end = ",")

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print(";")

#5. Reverse words in a sentence
def reverseString(s, start, end):
    while start < end:
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        start += 1
        end -= 1
    return "".join(s)

def reverseWords(s):
    if not s:
        return;
    arr = s.split()
    rst =""
    for word in arr:
        rst = rst + " " + reverseString(list(word), 0, len(word)-1)
    print(rst)

#6. String segmetation
def can_segment(s, dictionary):
    if not s:
        return False
    for i in range(len(s)):
        first = s[0:i]
        if first in dictionary:
            import pudb; pudb.set_trace()
            second = s[i:]
            if not second or \
               second in dictionary or \
               can_segment(second, dictionary):
                return True
        break
    return False

#7 Max Selling Profit
def max_profit_dp(arr):
    if not arr:
        return
    import sys
    max_profit = cur_profit = -sys.maxsize-1
    min_buy = arr[0]
    max_sell = arr[0]

    for i in range(1, len(arr)):
        cur_profit = arr[i] - min_buy
        if arr[i] < min_buy:
            min_buy = arr[i]

        if cur_profit > max_profit:
            max_profit = cur_profit
            max_sell = arr[i]

    return max_profit, max_sell - max_profit, max_sell

#8. Power
def power_cal(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    tmp = power_cal(x, n//2)
    if n % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp

def power(x, y):
    isNeg = False
    if y < 0:
        isNeg = True
        y = -1 * y
    rst = power_cal(x, y)

    if isNeq:
        return 1 / rst
    else:
        return rst

#9. subset
def subset(sets):
    lists = []
    cur=[]

    def subset_helper(li, index, rst, rsts):
        if index == len(li):
            rsts.append(list(rst))
            return

        rst.append(li[index])
        subset_helper(li, index+1, rst, rsts)

        rst.pop()
        subset_helper(li, index+1, rst, rsts)

    subset_helper(sets, 0, cur, lists)
    print(lists)

#10. Graph Clone
class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []

    def addNeighbor(node):
        self.neighbors.append(node)

def cloneGraph(root, cloned):
    newNode = Node(root.data)
    cloned[root] = newNode
    for p in root.neighbors:
        x = cloned.get(p)
        if x == None:
            newNode.addNeighbor(cloneGraph(p, cloned))
        else:
            newNode.addNeighbor(x)
    return newNode

#11. Serialize/Deserialize Tree
def give_me_sample_tree():

    n1 = TreeNode(100)
    n2 = TreeNode(50)
    n3 = TreeNode(200)

    n1.left = n2
    n1.right = n3
    n4 = TreeNode(25)
    n5 = TreeNode(75)
    n2.left = n4
    n2.right = n5

    n6 = TreeNode(30)
    n4.right = n6
    n7 = TreeNode(60)
    n5.left = n7
    n8 = TreeNode(125)
    n9 = TreeNode(350)
    n3.left = n8
    n3.right = n9

    return n1

MARKER = sys.maxsize
def serializeTree(root, stream):
    if root == None:
        stream.dump(MARKER)
        return
    stream.dump(root.data)
    serializeTree(root.left, stream)
    serializeTree(root.right, stream)


def deserializeTree(stream):
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None

        print("deserize: {}".format(data))
        node = TreeNode(data)
        node.left = deserializeTree(stream)
        node.right = deserializeTree(stream)
        return node
    except pickle.UnpicklingError:
        print("Error while pickling")
        return None

def serialize_tree_inorder(root, stream):
    if root == None:
        pickle.dump(MARKER, stream)
        return

    serialize_tree_inorder(root.left, stream)
    pickle.dump(root.data, stream)
    serialize_tree_inorder(root.right, stream)

def deserialize_tree_inorder(stream):
    try:
        data = pickle.load(stream)
        if data == MARKER:
            return None
        left_node = TreeNode(data)
        parent_node = deserialize_tree_inorder(stream)
        parent_node.left = left_node
        parent_node.right = deserialize_tree_inorder(stream)
    except pickle.UnpicklingError:
        print("Error while picking inorder")
        return None


# binary search in a rotated array
# 1. compare mid element and value
# 2, checking if mid element is in left half or right hard
def bi_search(arr, start, end, value):
    if start > end:
        return -1
    mid = start + (end -start) // 2
    if arr[mid] == value:
        return mid

    return -1

def bi_search_rotate(arr):
    return


if __name__ == '__main__':
    # 1. Move 0 to the left
    # v = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    # move_array_0_left(v)

    #2. Merge overlapping intervals
    # v = [Pair(1, 5), Pair(3, 1), Pair(4, 6), Pair(6, 8), Pair(10, 12), Pair(11, 15)]
    # result = merge_intervals(v)
    # for i in range(len(result)):
    #     print("[" + str(result[i].first) + ", " + str(result[i].second) + "]", end =" ")

#3. Convert binary tree to doubly linked list
    # from common.tree import TreeNode
    # n1 = TreeNode(100)
    # n2 = TreeNode(50)
    # n3 = TreeNode(200)

    # n1.left = n2
    # n1.right = n3
    # n4 = TreeNode(25)
    # n5 = TreeNode(75)
    # n2.left = n4
    # n2.right = n5

    # n6 = TreeNode(30)
    # n4.right = n6
    # n7 = TreeNode(60)
    # n5.left = n7
    # n8 = TreeNode(125)
    # n9 = TreeNode(350)
    # n3.left = n8
    # n3.right = n9

    # inorder(n1)

    # head, tail = convert_binary_tree(n1)
    # while head:
    #     print(head.data, end = ":")
    #     head = head.right

#4. Level order traversal of binary tree
    # level_traversal(n1)

#5. Reverse words in a sentence
    mystr = "Hello World"
    reverseWords(mystr)

    # print(mystr[0:4])
    # print(mystr[4:])

    # print(mystr[0:0])

#6. String segmentation
    # mystr = "hellonow"
    # import pudb; pudb.set_trace()
    # dictionary = set(["hello","hell","on","now"])
    # if can_segment(mystr, dictionary):
    #     print("String Can be Segmented")
    # else:
    #     print("String Can NOT be Segmented")

#7 Max Selling Profit
    # arr = [21, 12, 11, 9, 6, 3]
    # print(max_profit_dp(arr))

    subset([1, 2, 3])
    root = give_me_sample_tree()
    printByLevel(root)

    with open("tree.data", "wb") as fb:
        p = pickle.Pickler(fb)
        serializeTree(root, p)
    print("loading from tree.data......")

    with open("tree.data", "rb") as fb:
        newRoot = deserializeTree(fb)
        printByLevel(newRoot)

   v1 = [6, 7, 1, 2, 3, 4, 5];
   v2 = [4, 5, 6, 1, 2, 3];
