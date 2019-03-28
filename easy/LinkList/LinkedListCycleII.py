# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeDict = {}
        while head:
            if head in nodeDict:
                return head
            nodeDict[head] = 0
            head = head.next
        return None

    def detectCycle2(self, head):
        """
        所以head到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等。
        现在重新开始，head运行到环起点 和 相遇点到环起点 的距离也是相等的，相当于他们同时减掉了 环的起点到他们相遇的点的距离.
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:    
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next
        return None