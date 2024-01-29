class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        dp[i] = the most you can rob by going from house 1 to i
        since we can never go to house 1 & n at the same time,
        we return max(rob(1 to n-1), rob(2 to n))
        """

        def robWithoutCircle(nums):
            n = len(nums)
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[n-1]

        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])
        else: return max(robWithoutCircle(nums[1:]), robWithoutCircle(nums[:-1]))


        

        

        
