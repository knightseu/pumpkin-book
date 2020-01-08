# Equal Tree Partition
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

# Example
Example 1:

Input: {5,10,10,#,#,2,3}
Output: true
Explanation:
  origin:
     5
    / \
   10 10
     /  \
    2    3
  two subtrees:
     5       10
    /       /  \
   10      2    3
Example 2:

Input: {1,2,10,#,#,2,20}
Output: false
Explanation:
  origin:
     1
    / \
   2  10
     /  \
    2    20
    