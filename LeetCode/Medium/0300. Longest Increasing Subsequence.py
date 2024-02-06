class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (dp O(n^2))
        dp[i] = length of the longest incr subseq with last elem being nums[i]
        for each i, find the max dp[j] (j < i) where nums[j] < nums[i]
        """

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

        
