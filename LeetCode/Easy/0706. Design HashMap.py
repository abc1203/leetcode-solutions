class Node:
    def __init__(self, key=-1, val=-1, nxt=None):
        self.key = key
        self.val = val
        self.nxt = nxt

class MyHashMap(object):

    def __init__(self):
        self.n = 2500
        self.ht = [Node() for i in range(self.n)]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        prev, curr = self.ht[key%self.n], self.ht[key%self.n].nxt
        while curr:
            if curr.key == key: 
                curr.val = value
                return
            prev = prev.nxt
            curr = curr.nxt
        newNode = Node(key, value, None)
        prev.nxt = newNode
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        curr = self.ht[key%self.n].nxt
        while curr:
            if curr.key == key: return curr.val
            curr = curr.nxt
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        prev, curr = self.ht[key%self.n], self.ht[key%self.n].nxt
        while curr:
            if curr.key == key: prev.nxt = curr.nxt
            prev = prev.nxt
            curr = curr.nxt
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
