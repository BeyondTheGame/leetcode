# Definition for a binary tree node.
"""
Given a binary tree, find its minimum depth.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        基于层次遍历的思想  // BFS
        :param root:
        :return:
        """
        if not root:
            return 0
        queue = [(root, 1)]
        while len(queue) > 0:
            node, deep = queue.pop(0)
            if not node.left and not node.right:  # 没有子节点
                return deep
            if node.left:
                queue.append((node.left, deep+1))
            if node.right:
                queue.append((node.right, deep+1))

    # DFS
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:     # 左右子树都是空(叶节点)/   左右子树有一个为空
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:   # 左右子树均不为空
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth3(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        elif root.right and not root.left:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))