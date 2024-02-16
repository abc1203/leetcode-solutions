class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        idea (dp):
         - dp[i][j] = max coins from nums[i:j] ((left, right) => max coins)
        """

        dp = {}

        def backtrack(left, right):
            if left >= right: return 0

            for pivot in range(left, right):
                burst = nums[pivot]
                burst *= (nums[pivot-1] if pivot-1 >= left else 1)
                burst *= (nums[pivot+1] if pivot+1 < right else 1)

                burst = burst + backtrack(left, pivot) + backtrack(pivot+1, right)
                dp[(left, right)] = max(burst, dp.get((left, right), 0))
            print(dp)
            return dp[(left, right)]

        return backtrack(0, len(nums))


        
        
        
