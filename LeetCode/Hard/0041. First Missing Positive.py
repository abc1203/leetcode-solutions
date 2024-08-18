class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea:
         - alter nums so that nums[i] == i+1 for each nums[i] with 1 <= nums[i] <= len(nums)
         - do this at each i until it's good
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp

        for i in range(n):
            if nums[i] != i+1: return i+1
        return n+1
        





        
