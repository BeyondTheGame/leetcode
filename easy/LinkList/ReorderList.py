# Definition for singly-linked list.
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        Time Limit Exceeded
        1. 使用快慢指针来找到链表的中点，并将链表从中点处断开，形成两个独立的链表。
        2. 将第二个链翻转。
        3. 将第二个链表的元素间隔地插入第一个链表中。
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next     # 断开链表
        slow.next = None
        head_2 = last = mid     # 翻转后面的子链表
        while last.next:
            temp = last.next
            last.next = temp.next
            temp.next = head_2
            head_2 = temp
        head_1 = head
        while head_1 and head_2:
            temp = head_2
            temp.next = head_1.next
            head_1.next = temp
            head_2 = head_2.next
            head_1 = temp.next

    def reorderList2(self, head):
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head_2 = slow.next
        slow.next = None    # 断开
        stack = []
        while head_2:
            stack.append(head_2)
            head_2 = head_2.next
        head_1 = head
        while stack and head_1:
            temp = stack.pop()
            temp.next = head_1.next
            head_1.next = temp
            head_1 = temp.next

