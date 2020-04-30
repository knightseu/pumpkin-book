import unittest
from common.tree import TreeNode
from common.tree import genCompleteBinaryTree

# ####################################################
# special trees, such as: A tree has only one node; all nodes in the tree has only left/right children,
#  which look like linked lists; The root node is null. If performance is important, 
# a test case with a huge number of nodes should also be covered.
# #####################################################

class TreeTests(unittest.TestCase):
 
    def test_genCompleteBinaryTree(self):
        print("=== Testing genCompleteBinaryTree till level 3...")
        # test level 0
        self.assertEqual(None, genCompleteBinaryTree(0))

        # test level 1
        root = genCompleteBinaryTree(1)
        self.assertEqual(1, root.data)
        self.assertEqual(None, root.left)
        self.assertEqual(None, root.right)

        # test level 2
        root = genCompleteBinaryTree(2)
        self.assertEqual(1, root.data)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)

        leftN = root.left
        rightN = root.right
        self.assertEqual(2, leftN.data)
        self.assertEqual(3, rightN.data)
        
        # test level 3
        root = genCompleteBinaryTree(3)
        self.assertEqual(1, root.data)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)

        leftN = root.left
        rightN = root.right
        self.assertEqual(2, leftN.data)
        self.assertEqual(3, rightN.data)

        left2N = leftN.left
        right2N = leftN.right 
        self.assertIsNotNone(left2N)
        self.assertIsNotNone(right2N)

        self.assertEqual(4, left2N.data)
        self.assertEqual(5, right2N.data)

        left2N = rightN.left
        right2N = rightN.right 
        self.assertIsNotNone(left2N)
        self.assertIsNotNone(right2N)

        self.assertEqual(6, left2N.data)
        self.assertEqual(7, right2N.data)