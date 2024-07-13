class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max1, max2, min1, min2 = 0, 0, 0, 0

        max1, min1 = max(nums), min(nums)
        nums.remove(max1)
        nums.remove(min1)
        max2, min2 = max(nums), min(nums)
        return max1*max2 - min1*min2
