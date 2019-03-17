# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        from collections import deque
        deq = deque([(root, 1)])
        while deq:
            curr, value = deq.popleft()
            if not curr.left and not curr.right and not deq:
                return value
            if curr.left:
                deq.append((curr.left, value+1))
            if curr.right:
                deq.append((curr.right, value+1))

    def maxDepth3(self, root: TreeNode) -> int:
        def getMax(tree: TreeNode, currDepth):
            if not tree.left and not tree.right:
                return currDepth
            else:
                if not tree.left:
                    return getMax(tree.right, currDepth+1)
                elif not tree.right:
                    return getMax(tree.left, currDepth+1)
                else:
                    return max(getMax(tree.left, currDepth+1), getMax(tree.right, currDepth+1))

        if not root:
            return 0
        else:
            return getMax(root, 1)