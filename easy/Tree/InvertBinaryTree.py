# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        """
        :param root:
        :return:
        """
        if not root:
            return root
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            node.left, node.right = node.right, node.left
        return root

    def invertTree3(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        root.left, root.right = (self.invertTree(root.right), self.invertTree(root.left))
        return root