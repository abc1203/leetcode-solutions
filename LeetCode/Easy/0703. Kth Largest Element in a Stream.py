class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # min heap with k largest #s
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
