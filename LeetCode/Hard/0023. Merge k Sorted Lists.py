# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        approach:
         - merge l1 w/ l2, l3 w/ l4, ...
         - then merge the combined lists until one is left
        """

        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
            
            return dummy.next
        

        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                newLists.append(merge(l1, l2))
            lists = newLists
        
        return lists[0] if len(lists) == 1 else None
        
