"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node

        idea:
        iterate the org linked list twice - one for all the nodes & one for random
        create a hashmap with key = orig_node & val = new_node
        """

        m = {None: None}
        dummy = Node(0)

        curr, currCopy = head, dummy
        while curr:
            newNode = Node(curr.val)
            currCopy.next = newNode

            currCopy = currCopy.next
            m[curr] = currCopy
            curr = curr.next
        
        curr = head
        while curr:
            currCopy = m[curr]
            currCopy.random = m[curr.random]

            curr = curr.next
        
        return dummy.next



        
