class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        idea:
        dp[i][j] = dp[i-1][j] + dp[i][j-1] (if they're not obstacle)
        """

        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]

        for i in range(len(dp)):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for j in range(len(dp[0])):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if obstacleGrid[i][j] == 1: continue

                if obstacleGrid[i-1][j] == 0: dp[i][j] += dp[i-1][j]
                if obstacleGrid[i][j-1] == 0: dp[i][j] += dp[i][j-1]
        
        return dp[len(dp)-1][len(dp[0])-1]

        
