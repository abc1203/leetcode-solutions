class MyHashSet(object):

    def __init__(self):
        self.n = 1000
        self.ht = [[] for i in range(self.n)]
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.ht[key%self.n]: self.ht[key%self.n].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.ht[key%self.n]: self.ht[key%self.n].remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return (key in self.ht[key%self.n])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
