# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = fast = head
        last = slow
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        last.next = None
        root = TreeNode(slow.val)
        if head is not slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)
        return root

    """
    利用两个函数来进行递归
    """

    def sortedListToBST2(self, head):
        if not head:
            return None
        self.helper(head, None)

    def helper(self, head, tail):
        if head is tail:
            return None
        slow = fast = head
        while fast is not tail and fast.next is not tail:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.helper(head, slow)
        root.right = self.helper(slow.next, tail)
        return root