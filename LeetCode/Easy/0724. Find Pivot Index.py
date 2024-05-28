class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach:
         - compute total, then go through the indices from 0
         - for each iter, calculate rSum and check if equal
        """
        
        total = sum(nums)
        lSum = 0
        for i in range(len(nums)):
            rSum = total - lSum - nums[i]
            if lSum == rSum: return i
            if i < len(nums): lSum += nums[i]
        return -1

        
