class MedianFinder(object):
    '''
    heap sol:
     - keep 2 heaps; one having smaller half & one have larger half
     - minheap is for larger half & maxheap is for smaller half
    '''

    def __init__(self):
        self.largeHalf = [] #minheap    
        self.smallHalf = [] #maxheap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None

        - either small & large have same size or large has one more
        - if len(small) = len(large), move max of small to large and add to small
        - if len(small) < len(large), move min of large to small and add to large
        """
        if len(self.smallHalf) == len(self.largeHalf):
            heappush(self.largeHalf, -heappushpop(self.smallHalf, -num))
        else:
            heappush(self.smallHalf, -heappushpop(self.largeHalf, num))
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smallHalf) == len(self.largeHalf):
            return float(-self.smallHalf[0] + self.largeHalf[0]) / 2
        else:
            return self.largeHalf[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
