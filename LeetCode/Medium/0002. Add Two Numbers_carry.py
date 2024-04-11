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

        idea 1:
        iterate l1 & l2 to get n1 & n2 - O(max(l1.len, l2.len))
        then use n2 to get ans - O(max(l1.len, l2.len) + 1)
        => O(max(l1.len, l2.len))

        idea 2:
        use carry over & do all in the same loop
        """

        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            val = v1 + v2 + carry
            carry = val / 10
            newNode = ListNode(val%10)
            cur.next = newNode
            cur = cur.next
        
        return dummy.next
            


        
