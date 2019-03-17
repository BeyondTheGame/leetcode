"""
Given a binary tree, determine if it is height-balanced.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getNodeDeep(tree: TreeNode):
            if not tree:
                return 0

            stack = [(tree, 1)]
            while (len(stack)):
                node, deep = stack.pop(0)
                if node.left:
                    stack.append((node.left, deep + 1))
                if node.right:
                    stack.append((node.right, deep + 1))
            return deep
        if root == None:
            return True
        lHeight, rHeight = getNodeDeep(root.left), getNodeDeep(root.right)
        return abs(lHeight - rHeight) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def isBalanced2(self, root):
        def helper(tree):
            if tree == None:
                return 0, True
            heightL, lBalance = helper(tree.left)
            heightR, rBalance = helper(tree.right)
            if lBalance and rBalance and abs(heightL - heightR) <= 1:
                return max(heightL, heightR) + 1, True
            else:
                return -1, False
        h, is_balance = helper(root)
        return is_balance