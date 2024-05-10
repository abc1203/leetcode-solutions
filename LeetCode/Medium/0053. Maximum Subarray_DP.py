class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        approach #1 (DNC - O(nlogn)):
         - find max subarray with left & right
         - then compare with the max subarray that contains mid - take the larger one
         - doesn't work if the values are NOT unique
        
        approach #2 (DP - O(n)):
         - dp[i] = largest sum of nums[:i+1] that contains nums[i]
             = max(dp[i-1] + nums[i], nums[i])
        """

        ans = prev = nums[0]

        for i in range(1, len(nums)):
            curr = max(prev + nums[i], nums[i])
            ans = max(ans, curr)
            prev = curr
        
        return ans
