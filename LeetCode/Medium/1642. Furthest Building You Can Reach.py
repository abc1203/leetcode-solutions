class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int

        approach:
         - use ladder first and store the respective number into min heap
         - if no ladder and min(heap) < current diff, replace it with current diff
            (use ladder on the bigger step and bricks on the smaller step)
        """

        minHeap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]

            if diff > 0:
                if ladders > 0: 
                    ladders -= 1
                    heapq.heappush(minHeap, diff)
                elif minHeap and minHeap[0] < diff:
                    bricks -= heapq.heappop(minHeap)
                    heapq.heappush(minHeap, diff)
                else: bricks -= diff
            
            if bricks < 0: return i
    
        return len(heights)-1
        
        


        
