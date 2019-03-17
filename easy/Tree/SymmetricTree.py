# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        一种错误的思想，基于中序遍历的对称性是行不通的
        :param root:
        :return:
        """
        if root is None:
            return True

        def inOrder(tree: TreeNode):
            """
            中序遍历
            :param tree:
            :return:
            """
            in_order = []
            if tree.left is not None:
                in_order.extend(inOrder(tree.left))
            in_order.extend([tree.val])
            if tree.right is not None:
                in_order.extend(inOrder(tree.right))
            return in_order

        inorder = inOrder(root)
        nodeNum = len(inorder)
        for index in range(nodeNum//2):
            if inorder[index] != inorder[nodeNum-index-1]:
                return False
        return True

    def isSymmetric2(self, root):
        if not root:
            return True

        def dfs(left, right):
            if left and right:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
            return left == right
        return dfs(root.left, root.right)

    def isSymmetric3(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root]
        while queue:
            values = [node.val if node else None for node in queue]
            if values[::-1] != values:
                return False
            new_queue = []
            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
            queue = new_queue
        return True




tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(3)

solution = Solution()
symmetric = solution.isSymmetric(tree)
print(symmetric)