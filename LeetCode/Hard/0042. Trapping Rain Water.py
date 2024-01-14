class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        idea:
        consider water trapped between index left & right
        keep track of the max for left & right (left_max, right_max)
        case 1: left_max <= right_max, index_left_max <= left
        block indexed "left" would get left_max - height[left]
        case 2: left_max > right_max, index_right_max >= right
        block indexed "right" would get right_max - height[right]
        """

        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                ans += (left_max - height[left])
            elif left_max > right_max:
                right -= 1
                right_max = max(right_max, height[right])
                ans += (right_max - height[right])
        
        return ans
