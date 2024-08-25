class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        when we find a nums[i-1] > nums[i], there are a couple options:
         1. increase nums[i] so that nums[i-1] <= nums[i] <= nums[i+1]
         2. decrease nums[i-1] so taht nums[i-2] <= nums[i-1] <= nums[i]
        """
        n = len(nums)
        change = 1
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if change == 0: return False

                change = 0
                # check if increase nums[i] is possible
                if (i+1 < n and nums[i-1] <= nums[i+1]) or i+1 == n: 
                    nums[i] = nums[i-1]
                # check if decrease nums[i-1] is possible
                elif i-2 >= 0 and nums[i-2] <= nums[i]: 
                    nums[i-1] = nums[i-2]
                elif i-2 < 0: nums[i-1] = float('-inf')
                else: return False
        return True
        
