# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        idea:
         - traverse k first
         - move curr to k+1th node; then reverse the previous k
         - currHead points to end of reversed nodes each time
        """

        # x->1->2->3->y into x->3->2->1->y; takes x as input & return 1
        def reverse(prev, y):
            count = 1
            head = prev.next
            curr, nxt = head, head.next
            while count < k: # reverse 1->2->3 into 3->2->1
                tmp = nxt.next
                nxt.next = curr
                curr = nxt
                nxt = tmp
                count += 1
            prev.next = curr # x->3
            head.next = y # 1->y
            return head
        
        dummy = ListNode(next=head)
        curr, currHead = head, dummy
        count = 1
        while curr:
            if count == k: 
                curr = curr.next
                currHead = reverse(currHead, curr)
                count = 1
            if curr: curr = curr.next
            count += 1
        return dummy.next
