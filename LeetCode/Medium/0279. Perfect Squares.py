class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        idea:
         - first compute a list of perfect sqr nums
         - dp[i] = least # of perfect sqr nums that sum to i
             = 1 if i is a perfect sqr OR
             = min(dp[1]+dp[i-1], dp[4]+dp[i-4], ...)
        """

        sqrs = []
        i = 1
        while i * i <= n:
            sqrs.append(i * i)
            i += 1
        
        dp = [10001] * (n+1)
        for i in range(len(dp)):
            if i in sqrs: dp[i] = 1
            else:
                for num in sqrs:
                    if num <= i: dp[i] = min(dp[i], dp[num] + dp[i - num])
        
        return dp[n]



        
