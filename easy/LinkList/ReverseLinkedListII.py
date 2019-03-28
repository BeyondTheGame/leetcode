# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        counter = 0
        while counter < m-1:
            pre = pre.next
            counter += 1
        curr = pre.next
        counter = m
        while counter < n:
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next
            pre.next = temp
            counter += 1
        return dummy.next
