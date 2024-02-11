class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        idea (dp):
         - backtrack(i, curr_sum) = # of ways to get curr_sum using nums[:i]
         - backtrack(i, curr_sum) = backtrack(i+1, curr_sum+nums[i]) + 
         -                          backtrack(i+1, curr_sum-nums[i])
        """

        # (index, curr_sum) -> # of ways
        dp = {}

        def backtrack(i, curr_sum):
            if i >= len(nums) and curr_sum == target: return 1
            elif i >= len(nums): return 0
            
            if (i, curr_sum) in dp: return dp[(i, curr_sum)]

            pos_cases = backtrack(i+1, curr_sum + nums[i])
            neg_cases = backtrack(i+1, curr_sum - nums[i])

            dp[(i, curr_sum)] = pos_cases + neg_cases
            return dp[(i, curr_sum)]
        
        return backtrack(0, 0)
        
