"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
is changed to the original key plus sum of all keys greater than the original key in BST.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def sum(node: TreeNode):
            if not node:
                return
            sum(node.right)
            node.val += self._sum
            self._sum = node.val
            sum(node.left)
        self._sum = 0
        sum(root)
        return root

    """
       def convertBST(self, root: 'TreeNode') -> 'TreeNode':
    """

    def update_m(self, node, value=0):
        if node.right != None:
            value = self.update_m(node.right, value)
        value = node.val + value
        node.val = value
        if node.left != None:
            value = self.update_m(node.left, value)
        return value