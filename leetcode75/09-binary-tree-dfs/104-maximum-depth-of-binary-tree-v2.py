# 104. Maximum Depth of Binary Tree

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if not left:
            return right + 1
        elif not right:
            return left + 1
        else:
            return max(left, right) + 1


# root = [3,9,20,None,None,15,7]
# root = [1,None,2]
root = [25,10,40,8,13,30,42,6,None,None,15,26,None,None,49,1,7,None,None,None,None,None,None,None,None,None,None,None,None,45,51]

tree01node3 = TreeNode(3)
tree01node5 = TreeNode(5)
tree01node1 = TreeNode(1)
tree01node6 = TreeNode(6)
tree01node2 = TreeNode(2)
tree01node9 = TreeNode(9)
tree01node8 = TreeNode(8)
tree01node7 = TreeNode(7)
tree01node4 = TreeNode(4)

tree01node3.left = tree01node5
tree01node3.right = tree01node1
tree01node5.left = tree01node6
tree01node5.right = tree01node2
tree01node1.left = tree01node9
tree01node1.right = tree01node8
tree01node2.left = tree01node7
tree01node2.right = tree01node4


# queda pendiente como convertir la lista en una instancia de la clase TreeNode

solution = Solution()
# print(solution.maxDepth(root))
print(solution.maxDepth(tree01node3))
