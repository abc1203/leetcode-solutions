class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        idea #1:
        dp[i][j] = unique # of ways to get val j using nums[:i]
             = dp[i-1][j- k * nums[i-1]], k*nums[i-1] <= j
        
        implementation:    
            dp = [[0] * (target+1) for i in range(len(nums)+1)]
            for i in range(len(dp)): dp[i][0] = 1

            for i in range(1, len(dp)):
                for j in range(1, len(dp[i])):
                    k = 0
                    while k * nums[i-1] <= j:
                        dp[i][j] += dp[i-1][j - k * nums[i-1]]
                        k += 1

            return dp[len(nums)][target]
        
        idea #2:
        dp[i] = # of ways to get i using nums
        """

        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i-n]
        
        return dp[target]


        
