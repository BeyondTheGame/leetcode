# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        head = None
        curr = None
        while l1 and l2:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
                node.next = None
            else:
                node = l2
                l2 = l2.next
                node.next = None
            if head == None:
                head = curr = node
            else:
                curr.next = node
                curr = node
        if head:
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
        else:   # l1 或者 l2为空
            if l1:
                head = l1
            elif l2:
                head = l2
        return head
