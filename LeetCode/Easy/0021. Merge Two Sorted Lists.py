# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr_node, start_node = None, None
        while list1 or list2:
            if list1 == None:
                new_node = list2
                list2 = new_node.next
            elif list2 == None:
                new_node = list1
                list1 = new_node.next
            elif list1.val <= list2.val:
                new_node = list1
                list1 = new_node.next
            else:
                new_node = list2
                list2 = new_node.next
            
            if curr_node == None:
                curr_node = new_node
                start_node = curr_node
            else:
                curr_node.next = new_node
                curr_node = new_node
        
        return start_node

        
