# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        idea (one pass):
        1. let right be nth node from head
        2. define left & iterate until right reaches the end
        3. delete left
        """

        r = head
        while n > 0:
            r = r.next
            n -= 1
        
        l = head
        if not r: return l.next
        while r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return head
        
