class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        idea:
        get sum & divide by 2 to get the desired target => becomes 0/1 knapsack 
        dp[i][j] = whether it's possible to get j using 0 to i
        only need to find half since the other half will be automatically found
        """

        if sum(nums) % 2 == 1: return False

        target = sum(nums) / 2
        dp = [[False] * (target+1) for i in range(len(nums))]

        for i in range(len(dp)): dp[i][0] = True

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if j-nums[i] >= 0: dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i]])
                else: dp[i][j] = dp[i-1][j]
        
        return dp[len(dp)-1][len(dp[0])-1]
        
