# fb top 40 -educative
# https://www.educative.io/blog/cracking-top-facebook-coding-interview-questions#questions

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
    from common.tree import TreeNode
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
    mystr = "hellonow"
    import pudb; pudb.set_trace()
    dictionary = set(["hello","hell","on","now"])
    if can_segment(mystr, dictionary):
        print("String Can be Segmented")
    else:
        print("String Can NOT be Segmented")
