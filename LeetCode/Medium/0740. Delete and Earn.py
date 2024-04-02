class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (DP):
         - very similar to house robber problem
         - vals[i] = values you can get from taking i
         - dp[i] = max points from 0 to i = max(dp[i-2] + vals[i], dp[i-1]) (take or don't take)
        """

        vals = [0] * (max(nums)+1)
        dp = [0] * (max(nums)+1)
        
        for i in range(len(nums)):
            vals[nums[i]] += nums[i]
        
        dp[1] = vals[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-2] + vals[i], dp[i-1])
        
        return dp[len(dp)-1]
            



        
