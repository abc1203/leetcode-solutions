# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        idea:
        iterate l1 & l2 to get n1 & n2 - O(max(l1.len, l2.len))
        then use n2 to get ans - O(max(l1.len, l2.len) + 1)
        => O(max(l1.len, l2.len))
        """

        n1, n2 = 0, 0
        i = 0
        while l1 or l2:
            if l1:
                n1 += pow(10, i) * l1.val
                l1 = l1.next
            if l2:
                n2 += pow(10, i) * l2.val
                l2 = l2.next
            i += 1

        res = n1 + n2
        head = ListNode(0, None)
        if res == 0: return head
        
        currNode = head
        while res > 0:
            digit = res % 10
            newNode = ListNode(digit, None)
            currNode.next = newNode
            currNode = newNode
            res /= 10
        
        return head.next


        
