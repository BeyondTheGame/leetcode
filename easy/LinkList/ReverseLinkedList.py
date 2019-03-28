# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        last = head
        curr = head.next
        while last.next:
            last.next = curr.next
            curr.next = head
            head = curr
        return head

    def reverseList(self, head):
        """
        recursively
        :param self:
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        