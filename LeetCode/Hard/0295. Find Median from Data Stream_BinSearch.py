class MedianFinder(object):

    def __init__(self):
        self.stream = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        l, r = 0, len(self.stream)-1
        while l <= r:
            m = (l+r)/2
            if num == self.stream[m]: 
                self.stream.insert(m, num)
                return
            elif num < self.stream[m]: r = m-1
            else: l = m+1
        self.stream.insert(l, num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.stream)
        if n % 2 == 0:
            l, r = n/2-1, n/2
            return float(self.stream[l]+self.stream[r])/2
        else:
            idx = n/2
            return self.stream[idx]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
