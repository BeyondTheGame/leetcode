# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        将每个节点都当成根节点和非根节点来考虑
        :param root:
        :param sum:
        :return:
        """
        def findpath(tree: TreeNode, currsum: int):
            if not tree:
                return 0
            return (currsum == tree.val) + findpath(tree.left, currsum-tree.val) + findpath(tree.right, currsum-tree.val)
        if not root:
            return 0
        return findpath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        """
        Time Limit Exceeded
        :param root:
        :param sum:
        :return:
        """
        def findpath(tree: TreeNode, res, currSum, sum, path):
            if not tree:
                return
            currSum += tree.val
            path.append(root.val)
            if currSum == sum:
                res[0] += 1
            temp = currSum
            for ele in path:
                temp -= ele
                if temp == sum:
                    res[0] += 1
                    break
            findpath(root.left, res, currSum, sum, path)
            findpath(root.right, res, currSum, sum, path)
            path.pop()
        res = [0]
        currSum = 0
        findpath(root, res, currSum, sum, [])
        return res[0]