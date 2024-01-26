# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.

        idea:
        1. find middle of list using tortoise & hare
        2. reverse the 2nd half of list
        3. go one for one for the reorder
        """

        # tortoise and hare
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse with prev as head
        curr, prev = slow, None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # go 1 for 1
        curr1, curr2 = head, prev
        while curr1:
            next_node = curr1.next
            if curr2:
                curr1.next = curr2
                curr2 = curr2.next
                curr1.next.next = next_node 
            curr1 = next_node
            
        return head
        
