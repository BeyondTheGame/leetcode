# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num, count = 0, 0
        while l1:
            num += pow(10, count) * l1.val
            l1 = l1.next
            count += 1
        count = 0
        while l2:
            num += pow(10, count) * l2.val
            l2 = l2.next
            count += 1
        re = ListNode(0)
        if num > 0:
            currNode = re
            while num > 0:
                currNode.val = num % 10
                num = num // 10
                if num > 0:
                    newNode = ListNode  # new 一个新节点
                    currNode.next = newNode
                    currNode = newNode

        return re

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0  # 进位
        head = l1
        curr = l1
        while l1 and l2:
            curr = l1
            sum = l1.val+l2.val + carry
            curr.val = sum % 10
            carry = sum // 10
            l1, l2 = l1.next, l2.next
        if l2:  # l2比l1长
            curr.next = l2
            l1 = l2
        while l1:
            curr = l1
            sum = l1.val + carry
            curr.val = sum % 10
            carry = sum // 10
            l1 = l1.next
        if carry > 0:
            newNode = ListNode(carry)
            curr.next = newNode
        return head

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, val = 0, 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            curr.val = val
            if l1 or l2:
                curr.next = ListNode(0)
                curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy