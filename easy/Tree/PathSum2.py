# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursively
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        def findOnePath(tree: TreeNode, sum: int, onepath=[]):
            if not root.left and not root.right and tree.val == sum:
                onepath.append(tree.val)
                self.res.append(onepath)
            if tree.left:
                findOnePath(tree.left, sum-tree.val, onepath+[tree.val])
            if tree.right:
                findOnePath(tree.right, sum-tree.val, onepath+[tree.val])
            return 0
        if not root:
            return []
        self.res = []
        findOnePath(root, sum)
        return self.res

    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        if not root:
            return []
        elif not root.left and not root.right and sum == root.val:
            return [[root.val]]
        res = []
        l = self.pathSum(root.left, sum - root.val)
        r = self.pathSum(root.right, sum - root.val)
        for i in l:
            res.append([root.val] + i)
        for i in r:
            res.append([root.val] + i)
        return res

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        tmp = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]

    # BFS
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        queue = [(root, sum-root.val, [root.val])]
        while queue:
            node, sumval, ls = queue.pop(0)
            if not node.left and not node.right:    # leaf node
                if sumval == 0:
                     res.append(ls)
            if node.left:
                queue.append((node.left, sumval-node.left.val, ls + [node.left.val]))
            if node.right:
                queue.append((node.right, sumval-node.right.val, ls + [node.right.val]))
        return res

    # stack + DFS
    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            node, sumval, ls = stack.pop()
            if not node.left and not node.right and sumval == 0:
                res.append(ls)
            if node.right:
                stack.append((node.right, sumval-node.right.val, ls+[node.right.val]))
            if node.left:
                stack.append((node.left, sumval-node.left.val, ls+[node.left.val]))
        return res

    def pathSum(self, root: TreeNode, _sum: int) -> list[list[int]]:
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            currnode, ls = stack.pop()
            if not currnode.left and not currnode.right and sum(ls) == _sum:
                res.append(ls)
            if currnode.right:
                stack.append((root.right, ls+[root.right.val]))
            if currnode.left:
                stack.append((root.left, ls+[root.left.val]))
        return res