class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        idea (dp):
        dp[i][j] = # of ways to get to (i, j) = dp[i-1][j] + dp[i][j-1]
        """

        dp = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0: dp[i][j] = 1
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        
