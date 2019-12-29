# Subtree
Description
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

# Example
Example 1:

Input：{1,2,3,#,#,4},{3,4}
Output：true
Explanation：
T2 is a subtree of T1 in the following case:
           1                3
          / \              / 
    T1 = 2   3      T2 =  4
            /
           4
Example 2:

Input：{1,2,3,#,#,4},{3,#,4}
Output：false
Explanation：
T2 isn't a subtree of T1 in the following case:

           1               3
          / \               \
    T1 = 2   3       T2 =    4
            /
           4
           