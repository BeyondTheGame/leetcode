# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
    """
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums or len(nums) == 0:
            return None
        numsLen = len(nums)
        if numsLen == 1:
            return TreeNode(nums[0])
        else:
            tree = TreeNode(nums[numsLen // 2])
            tree.left = self.sortedArrayToBST(nums[:numsLen // 2])
            tree.right = self.sortedArrayToBST(nums[numsLen // 2 + 1:])
            return tree

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid-1)
            node.right = convert(mid+1, right)
            return node
        return convert(0, len(nums)-1)