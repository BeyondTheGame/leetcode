# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        slow fast pointer + stack
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        stack = []
        slow = fast = head
        stack.append(head.val)
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        if not fast.next:   # 链表长度是基数
            stack.pop()
        while slow.next:
            slow = slow.next
            value = stack.pop()
            if value != slow.val:
                return False
        return True

    def isPalindrome2(self, head):
        """
         O(1) space
         可以在找到中点后，将后半段的链表翻转一下，这样我们就可以按照回文的顺序比较了.
        :param head:
        :return:
        """
        if not head or not head.next:
            return True
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        last = slow.next
        pre = head
        while last.next:
            temp = last.next
            last.next = temp.next
            temp.next = slow.next
            slow.next = temp
        while slow.next:
            slow = slow.next
            if slow.val != pre.val:
                return False
            pre = pre.next
        return True



