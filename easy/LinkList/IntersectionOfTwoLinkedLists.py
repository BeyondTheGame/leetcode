# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB : ListNode):
        """
        如果两个链长度相同的话，那么对应的一个个比下去就能找到。所以只需要把长链表变短即可。
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA = self.getListLength(headA)
        lenB = self.getListLength(headB)
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        i = 0
        while i < lenA - lenB:
            headA = headA.next
            i += 1
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getListLength(self, head: ListNode):
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode):
        """
        这道题还有一种特别巧妙的方法，虽然题目中强调了链表中不存在环，但是我们可以用环的思想来做，
        我们让两条链表分别从各自的开头开始往后遍历，当其中一条遍历到末尾时，我们跳到另一个条链表的开头继续遍历。
        两个指针最终会相等，而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各自的末尾的空节点处相等。
        为什么一定会相等呢，因为两个指针走过的路程相同，是两个链表的长度之和 或者 ...，所以一定会相等
        :param headA:
        :param headB:
        :return:
        """
        if None in (headA, headB):
            return None
        nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            if nodeA is None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB is None:
                nodeB = headA
            else:
                nodeB = nodeB.next

        return nodeA

headA = ListNode(0)
headA.next = ListNode(9)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)

headB = ListNode(3)
headB.next = ListNode(2)
headB.next.next = ListNode(4)

solution = Solution()
solution.getIntersectionNode2(headA, headB)