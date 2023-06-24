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


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # Initial definition of Solution
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         return 0


class Solution:
    def maxDepth(self, root: List) -> int:
        return 0

def calcular_niveles(elements: int):
    sumatoria = 0
    n = 0
    while sumatoria < elements:
        sumatoria += 2 ** n
        n += 1
    return n


# root = [3,9,20,None,None,15,7]
# root = [1,None,2]
root = [25,10,40,8,13,30,42,6,None,None,15,26,None,None,49,1,7,None,None,None,None,None,None,None,None,None,None,None,None,45,51]

print(calcular_niveles(len(root)))

# solution = Solution()
# print(solution.maxDepth(root))
