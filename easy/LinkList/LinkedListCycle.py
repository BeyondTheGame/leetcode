# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        O(n) extra space
        :type head: ListNode
        :rtype: bool
        """
        nodeDict = {}
        while head:
            if head in nodeDict:
                return True
            nodeDict[head] = 0
            head = head.next
        return False


    def hasCycle2(self, head:ListNode):
        """
        经典的two poiters method
        只需要设两个指针，一个每次走一步的慢指针和一个每次走两步的快指针，如果链表里有环的话，两个指针最终肯定会相遇。
        因为fast的速度是slow的两倍，所以fast走的距离是slow的两倍
        :param head:
        :return:    如果fast遇到null，则说明没有环，返回false; 如果slow==fast，说明有环，并且此时fast超了slow一圈.
        为什么有环的情况下二者一定会相遇呢？因为fast先进入环，在slow进入之后，如果把slow看作在前面，
        fast在后面每次循环都向slow靠近1，所以一定会相遇，而不会出现fast直接跳过slow的情况。
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
            return False