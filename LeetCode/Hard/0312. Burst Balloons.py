class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (dp):
         - choosing a pivot to pop first doesn't work bc now the 2 parts are indep
         - instead choose a pivot to pop last
         - then dp[(left, right)] = val for popping last + dp[(left, pivot)] + dp[(pivot, right)]
         - note that indices for left & right are inclusive
        """

        nums = [1] + nums + [1]
        dp = {}

        for offset in range(2, len(nums)):
            for left in range(0, len(nums)-offset):
                right = left + offset

                for pivot in range(left+1, right):
                    burst = nums[left] * nums[pivot] * nums[right]
                    burst += dp.get((left, pivot), 0) + dp.get((pivot, right), 0)
                    dp[(left, right)] = max(burst, dp.get((left, right), 0))
        
        return dp.get((0, len(nums)-1), 0)


        
        
        
