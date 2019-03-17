# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        """
        从底向上的层次遍历
        :param root:
        :return:
        """
        re = []
        if not root:
            return re
        currLevel = [root]
        while len(currLevel) > 0:
            nextLevel = []
            currLevelValue = []
            for element in currLevel:
                currLevelValue.append(element.val)
                if element.left:
                    nextLevel.append(element.left)
                if element.right:
                    nextLevel.append(element.right)
            re.insert(0, currLevelValue)
            currLevel = nextLevel
        return re

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(3)

solution = Solution()
symmetric = solution.levelOrderBottom(tree)
print(symmetric)