class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        idea:
         - sort intervals and record end times using min heap
         - if start(new) < min(heap), need new room
         - else replace the min(heap) room with current node
         - add new node to record new end time to heap
        """

        intervals.sort()
        ans = 0
        minHeap = []

        for start, end in intervals:
            if len(minHeap) == 0 or start < minHeap[0]: 
                ans += 1
            else:
                heappop(minHeap)
            heappush(minHeap, end)
        return ans
        
