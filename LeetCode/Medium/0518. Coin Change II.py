class Solution(object):
    def change(self, amount, coins):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        idea (dp):
         - dp[i][j] = # of ways to make up amount i using coins[0:j]
         - dp[i][j] = dp[i][j-1] + dp[i - coins[j-1]][j-1]
        """
        
        dp = [[0] * (len(coins)+1) for i in range(amount+1)]
        for j in range(len(dp[0])): dp[0][j] = 1

        for i in range(1, amount+1):
            for j in range(1, len(coins)+1):
                if coins[j-1] <= i:
                    dp[i][j] = dp[i][j-1] + dp[i - coins[j-1]][j]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[amount][len(coins)]

        
        
