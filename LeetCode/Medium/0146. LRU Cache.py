class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {} # key : Node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node
    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node from right
    def insertNode(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev, node.next = prev, self.right
        self.right.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.insertNode(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None

        # 1. update if already exists
        # 2. evict + add if full
        # 3. add if not full
        """

        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            node.val = value
            self.insertNode(node)
        elif len(self.cache) >= self.capacity:
            leftNode = self.left.next
            self.removeNode(leftNode)
            del self.cache[leftNode.key]

            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertNode(newNode)
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insertNode(newNode)
        

        






        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
