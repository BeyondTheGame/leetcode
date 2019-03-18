# Definition for a binary tree node.

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf
path such that adding up all the values along the path equals the given sum.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:   # leaf node
            return True
        elif not root.left:     # 只有左边子树为空
            return self.hasPathSum(root.right, sum-root.val)
        elif not root.right:    # 只有右边子树为空
            return self.hasPathSum(root.left, sum-root.val)
        else:   # 左右子树均不为空
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

    def hasPathSum2(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # BFS with queue
    def hasPathSum3(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, value = queue.pop(0)
            if not curr.left and not curr.right:
                if value == 0:
                    return True
            if curr.left:
                queue.append((curr.left, value-curr.left.val))
            if curr.right:
                queue.append((curr.right, value-curr.right.val))
        return False