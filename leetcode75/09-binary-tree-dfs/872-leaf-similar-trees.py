# 872. Leaf-Similar Trees

'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.


For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).


Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 1. ubicar los nodos hojas y agregarlos en una lista
        # 2. hacer lo mismo en el arbol 2
        # 3. comparar las listas si son iguales en valores y posicion
        list1 = []
        list2 = []

        dfs(root1, list1)
        dfs(root2, list2)
        print("list1 ", list1)
        print("list2 ", list2)

        return True if list1 == list2 else False
    

def dfs(root: Optional[TreeNode], leaf_list: List):
    if root.left == None and root.right == None:
        leaf_list.append(root.val)
    if root.left != None:
        dfs(root.left, leaf_list)
    if root.right != None:
        dfs(root.right, leaf_list)


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

tree02node3 = TreeNode(3)
tree02node5 = TreeNode(5)
tree02node1 = TreeNode(1)
tree02node6 = TreeNode(6)
tree02node2 = TreeNode(2)
tree02node7 = TreeNode(7)
tree02node4 = TreeNode(4)
tree02node9 = TreeNode(9)
tree02node8 = TreeNode(8)

tree02node3.left = tree02node5
tree02node3.right = tree02node1
tree02node5.left = tree02node6
tree02node5.right = tree02node7
tree02node1.left = tree02node4
tree02node1.right = tree02node2
tree02node2.left = tree02node9
tree02node2.right = tree02node8

solution = Solution()
print(solution.leaf_similar(tree01node3, tree02node3))
