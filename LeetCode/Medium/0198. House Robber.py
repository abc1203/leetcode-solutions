class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        dp[i] = the most you can rob by going from house 1 to i
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        """

        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[len(dp)-1]

        
