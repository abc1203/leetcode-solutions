class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        idea 1: divide and conquer O(nlogn)
        1. compute the max area for left & right half
        2. compute the max area that involves crossing the left & right half
        """

        if len(heights) == 1: return heights[0]
        
        mid = len(heights) / 2
        max_area = max(self.largestRectangleArea(heights[:mid]), 
                        self.largestRectangleArea(heights[mid:]))
        
        # start with (mid-1, mid) and always choose the taller one
        l, r = mid-1, mid
        min_height = min(heights[l], heights[r])
        area = min_height * 2
        while l > 0 or r < len(heights)-1:
            if r >= len(heights)-1 or (l-1>=0 and heights[l-1] >= heights[r+1]):
                l -= 1
                min_height = min(min_height, heights[l])
                area = max(area, min_height * (r-l+1))
            else:
                r += 1
                min_height = min(min_height, heights[r])
                area = max(area, min_height * (r-l+1))
        
        return max(max_area, area)

        

        

        
