# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        approach O(1) space:
        tortoise and hare method
        """

        tortoise = hare = head

        while hare:
            hare = hare.next
            if hare:
                hare = hare.next
            else:
                return False
            tortoise = tortoise.next
            if tortoise == hare: return True
        
        return False
        
