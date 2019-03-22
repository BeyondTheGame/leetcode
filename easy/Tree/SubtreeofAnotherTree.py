# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSameTree(p, q):
            if p == None and q == None:
                return True
            elif p != None and q != None:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else:
                return False

        if not t:
            return True
        if not s:
            return False
        return isSameTree(s, t) or isSameTree(s.left, t) or isSameTree(s.right, t)

    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        serialize_S = self.serialize(s)
        serialize_T = self.serialize(t)
        if serialize_S == serialize_T:
            return True
        for index in range(len(serialize_S)-len(serialize_T)):
            if serialize_T == serialize_S[index:index+len(serialize_T)]:
                return True
        return False

    def serialize(self, tree: TreeNode):    # 后序序列化
        res = []
        if not tree:
            return [None]
        res += self.serialize(tree.left)
        res += self.serialize(tree.right)
        res += [tree.val]
        return res