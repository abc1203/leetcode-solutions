class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int

        idea (O(N)):
         - dp[i] = max product for i
        """

        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, int(i/2)+1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        return dp[n]

        
