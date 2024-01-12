class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        algo: 
        1. use 2 pointers - one from start & one from end
        2. left shorter => move start to the right
        3. right shorter => move end to the left
        """
        max_area = 0
        start, end = 0, len(height)-1

        while start < end:
            area = min(height[start], height[end]) * (end - start)
            if area > max_area: max_area = area

            if height[start] <= height[end]: start += 1
            else: end -= 1
        
        return max_area
